

cur_frm.cscript.refresh = function(frm){
		cur_frm.set_df_property("cost_center", "hidden", true);
}

cur_frm.fields_dict["expenses"].grid.get_field("cost_center").get_query = function(doc){
       return {
               filters:{

					   "is_group": "child"
               }
       }
}


frappe.ui.form.on("Expense Claim", "onload", function(frm) {
    cur_frm.set_query("travel_request_reference", function() {
        return {
            "filters": {
                "employee": frm.doc.employee
            }
        };
    });
});
