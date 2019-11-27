
frappe.ui.form.on('Expense Claim Type', {
	deferred_expense_account: function(frm) {
	var flag = frm.doc.deferred_expense_account;

	frm.fields_dict["accounts"].grid.get_field("default_account").get_query = function(frm, cdt, cdn){
	var d = locals[cdt][cdn];

		return{
			filters: {
				"is_group": 0,
				"root_type": cur_frm.doc.deferred_expense_account ? "Asset" : "Expense",
				'company': d.company
			}
		}
	}

	}

});
