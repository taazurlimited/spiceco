
//user filter for travel request status
cur_frm.cscript.onload = function() {
    frappe.call({
            method:"spiceco.travel_approver.get_user",
            args: {
                'user': frappe.user_roles
            },
            callback: function(r){
            console.log(r.message);
                var result = [];
                for (var i = 0; i < r.message.length; i++) {
                    result.push(r.message[i]);
                   }
                cur_frm.set_df_property('approval_status', 'options', [""].concat(result));
                cur_frm.refresh_field('approval_status');

            }
        });
  }




//travel approver
cur_frm.cscript.employee = function( doc, cdt, cdn) {
    var d = locals[cdt][cdn];
    console.log(d);
    frappe.call({
            method:"spiceco.travel_approver.get_approvers",
            args: {
                'employee': d.employee
            },
            callback: function(r){
                var result = [];
                for (var i = 0; i < r.message.length; i++) {
                    result.push(r.message[i].approver);
                   }
                cur_frm.set_df_property('travel_approver', 'options', [""].concat(result));
                cur_frm.refresh_field('travel_approver');

            }
        });

}

///////////////////////////////////////////
frappe.ui.form.on("Travel Request", {
    refresh: function (frm) {
        if (cur_frm.doc.docstatus == 1 && cur_frm.doc.travel_status == "Completed"){
            cur.frm.disable_("Make Advance Payment");
        }

        if(cur_frm.doc.docstatus == 1 && cur_frm.doc.itinerary.length >= 1) {
            if (itinerary() >= 1){
            //console.log (cur_frm.doc.docstatus == 1 && cur_frm.doc.itinerary.length >= 1);
            //var itinerary = itinerary(frm)
            cur_frm.add_custom_button(__("Make Advance Payment"), function() {
			frappe.model.open_mapped_doc({
    			method: "spiceco.travel_approver.make_employee_advance",
    			frm: cur_frm
    		})

            });
            }//close second if
        } //close first if


    }
})

function itinerary(frm){
    var itinerary = 0;
        if (cur_frm.doc.itinerary.length >= 1){
            for (var i = 0; i < cur_frm.doc.itinerary.length; i++ ){
                itinerary += parseInt(cur_frm.doc.itinerary[i].travel_advance_required);
            }
        }
    return itinerary
}

cur_frm.cscript.validate = function(frm){
    var total_amount = 0;
        if (cur_frm.doc.itinerary.length >= 1){
            for (var i = 0; i < cur_frm.doc.itinerary.length; i++ ){
            if  (!cur_frm.doc.itinerary[i].advance_amount){
                continue;
            }
            else{
                //itinerary += parseInt(cur_frm.doc.itinerary[i].travel_advance_required);
                total_amount += parseInt(cur_frm.doc.itinerary[i].advance_amount);
                }
            }
            cur_frm.set_value("advance_amount", total_amount);
            //console.log(total_amount);
        }

}


///////////////////////////////////////////

