frappe.ui.form.on('Salary Slip',  'leave_without_pay',  function(frm) {
    frappe.call({
        method: "spiceco.salary_slip.check_hr_leave_without_pay",

        callback: (response) => {
            if(response.message!=1){
                frappe.msgprint("Leave Without Pay does not match with approved Leave Application records");
                frm.doc.leave_without_pay=0.00;
                cur_frm.refresh_field('leave_without_pay');
            }
        }
    });
});