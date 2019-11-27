frappe.ui.form.on('Loan Application',  'before_submit',  function(frm) {
    frappe.call({
	method: "spiceco.loan_application.validate_submission",
	args:{
	    'applicant': frm.doc.applicant,
	    'loan_type': frm.doc.loan_type
	},
	callback: (response) => {
	    if(parseInt(response.message)){
	        frappe.validated = false;
		    frappe.throw("Cannot submit loan applications for this applicant with an outstanding loan and the same loan type.");
	    }

	}
});
});