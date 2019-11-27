 frappe.listview_settings['Travel Request'] = {
        add_fields: ["status", "advance_amount", "travel_status", "travel_type", "approval_status"],
        get_indicator: function(doc) {
            if(doc.advance_amount >= 1 && doc.travel_status == "Travelling") {
                return [__("Travelling"), "orange", "status,=,Travelling"];
            }
            if(doc.advance_amount == 0) {
                return [__("Submitted"), "blue", "status,=,Submitted"];
            }
            else if(doc.travel_status == "Completed") {
                return [__("Completed"), "green", "status,=,Completed"];
            }
        }
 }



