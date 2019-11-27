import frappe

@frappe.whitelist()
def check_hr_leave_without_pay():
    leave_without_pay=frappe.db.sql("""Select value from `tabSingles` where doctype='HR Settings' and field='leave_without_pay'""")
    return leave_without_pay