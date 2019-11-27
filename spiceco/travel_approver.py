import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def get_approvers(employee):
	parentfield = "travel_approver"
	department = frappe.db.sql("""select department from `tabEmployee` where name= %s""",employee,as_dict=True)
	#dd = frappe.db.sql("""select user.name, user.first_name, user.last_name from
				#tabUser user, `tabDepartment Approver` approver where
				#approver.parent = %s and approver.parentfield = %s""",(department[0]['department'], parentfield), as_list=True)
	travel_approver = frappe.db.sql("""select approver from `tabDepartment Approver`  where parent = %s and parentfield = %s""", (department[0]['department'], parentfield), as_dict=True)

	print("+++++++++++++++++++++++++++++")
	print(department)
	print("+++++++++++++++++++++++++++++++")
	print(travel_approver)
	return travel_approver


@frappe.whitelist()
def make_employee_advance(source_name, target_doc=None):
	target_doc = get_mapped_doc("Travel Request", source_name,
        		{"Travel Request": {
        				"doctype": "Employee Advance",
        				"field_map": {
        					"employee": "employee",
							"purpose_of_travel": "purpose",
							"advance_amount": "advance_amount",
							"name": "travel_request"
        				}
        			}
				},target_doc)


	return target_doc

@frappe.whitelist()
def get_user(user):
	if "Travel Approver" in user:
		options = ["Open","Approved", "Rejected", "Cancelled"]

		return (options)
	else:
		options = ["Open"]
		return (options)






