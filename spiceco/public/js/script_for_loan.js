frappe.ui.form.on('Loan',  'validate',  function(frm) {
    frappe.call({
        method: "spiceco.loan.validate",
        args:{
            'applicant': frm.doc.applicant,
            'loan_amount': frm.doc.loan_amount
        },
        callback: (response) => {
            if(parseInt(response.message)){
                frappe.validated=false;
                frappe.throw("Loan amount should be less than or equal to applicant's assigned base salary.")
            }

        }
    });
});

frappe.ui.form.on('Loan',  {
    
    refresh: function(frm) {
        if ((!frappe.user.has_role("Administrator") || !frappe.user.has_role("HR Manager")) && frm.doc.docstatus==1){
            // read only status for non authorized user
            frm.set_df_property("loan_repayment_period_in_months", "read_only", 1);
            frm.set_df_property("loan_repayment_start_date", "read_only", 1);
            cur_frm.get_field("loan_repayment_schedule").grid.fields_map.payment_date1.read_only=1;            
        }
        if(frm.doc.docstatus==1){
            // hide standard fields during submit status and show custom fields
            frm.set_df_property("repayment_periods", "hidden", 1);
            frm.set_df_property("repayment_start_date", "hidden", 1);
            frm.set_df_property("repayment_schedule", "hidden", 1);
            frm.set_df_property("loan_repayment_period_in_months", "hidden", 0);
            frm.set_df_property("loan_repayment_start_date", "hidden", 0);
            frm.set_df_property("loan_repayment_schedule", "hidden", 0);
            
        }else{
            // show standard fields during draft status and hide custom fields
            frm.set_df_property("loan_repayment_period_in_months", "hidden", 1);
            frm.set_df_property("loan_repayment_start_date", "hidden", 1);
            frm.set_df_property("loan_repayment_schedule", "hidden", 1);
            frm.set_df_property("repayment_schedule", "hidden", 0);
            frm.set_df_property("repayment_periods", "hidden", 0);
            frm.set_df_property("repayment_start_date", "hidden", 0);
        }
        if(frm.doc.loan_repayment_period_in_months!=frm.doc.repayment_periods && frm.doc.docstatus!=1){
            // during draft, update loan repayment period if it's not equal to its standard field
            frm.doc.loan_repayment_period_in_months=frm.doc.repayment_periods;
            frm.refresh_field('loan_repayment_period_in_months');
            frm.save();
        }

        if(frm.doc.loan_repayment_start_date!=frm.doc.repayment_start_date && frm.doc.docstatus!=1){
            // during draft, update loan repayment start date if it's not equal to its standard field
            frm.doc.loan_repayment_start_date=frm.doc.repayment_start_date;
            frm.refresh_field('loan_repayment_start_date');
            frm.save();
        }
        
        
            
    },
    after_save: function(frm){
        if(frm.doc.docstatus == 1){
            // loan repayment schedule changed on submit status
            frappe.call({
                method: "spiceco.loan.update_repayment_sched",
                args:{
                    'name': frm.doc.name,
                    'rp': frm.doc.loan_repayment_period_in_months,
                    'rsd': frm.doc.loan_repayment_start_date
                },
                callback: (response) => {
                    frm.reload_doc();
                }
            });
        }else{
            frappe.call({
                method: "spiceco.loan.generate_data_for_lrs",
                args:{
                    'name':frm.doc.name
                },
                callback: function(response){
                    frm.reload_doc();
                }
            })
        }
        
    }
    
});
frappe.ui.form.on('Loan Repayment Schedule',  {
    'payment_date1': function(frm,dt,dn) {
        locals['Repayment Schedule'][locals[dt][dn].source].payment_date=locals[dt][dn].payment_date1;
    
        frappe.call({
            method: "spiceco.loan.set_repayment_schedule",
            args:{
                'name': dn,
                'source': locals[dt][dn].source,
                'parent': frm.doc.name,
                'payment_date': locals[dt][dn].payment_date1
            },
            callback: function(response){
                
                // Object.defineProperty(locals['Repayment Schedule'], response.message,Object.getOwnPropertyDescriptor(locals['Repayment Schedule'], cur_frm.doc.repayment_schedule[0].name));
                // delete locals['Repayment Schedule'][cur_frm.doc.repayment_schedule[0].name];
                // locals['Repayment Schedule'][response.message].name=response.message;
                // console.log(response.message);
                // locals[dt][dn].source=response.message;
                // locals['Repayment Schedule'][response.message].payment_date=locals[dt][dn].payment_date1;
                
            }
        })
    }
});



