import frappe
#from erpnext.hr.doctype.expense_claim.expense_claim import ExpenseClaim


#def get_gl_entries():
   # print("Hello")


#def expense_claim_save(doc, method):
    #ExpenseClaim.get_gl_entries = get_gl_entries
    #print(doc)


def gl_entry_save(doc, method):
    print(doc.__dict__)
    # list = []
    # voucher_number = doc.__dict__['voucher_no']
    #
    #
    # print("im expense" if doc.__dict__['voucher_type'] == "Expense Claim" else "not expense")
    # if (doc.__dict__['cost_center'] is None):
    #     print("cost center is none")
    #
    # else:
    #     print(doc.__dict__['cost_center'])
    #
    #
    # cost_center = frappe.db.sql("""SELECT `cost_center` FROM `tabExpense Claim Detail` """)
    #
    # print(cost_center)

#Travel Request
@frappe.whitelist()
def submit_tr(doc, method):
    if doc.docstatus == 1 and doc.approval_status == "Open":
        frappe.throw("""Approval Status must be 'Approved' or 'Rejected'""")

    elif doc.docstatus == 1 and doc.approval_status == "Approved" and doc.advance_amount > 0:
        frappe.db.sql("""UPDATE `tabTravel Request` SET `travel_status`=%s, `status`=%s where `name`=%s""", ("Travelling","Travelling", doc.name))
        frappe.db.commit()

    elif doc.docstatus == 1 and doc.approval_status == "Approved" and doc.advance_amount == 0:
        frappe.db.sql("""UPDATE `tabTravel Request` SET `travel_status`=%s, `status`=%s where `name`=%s""", ("Travelling","Submitted", doc.name))
        frappe.db.commit()

#Expense Claim
@frappe.whitelist()
def submit_expense(doc, method):

    if doc.docstatus == 1 and doc.approval_status != "Rejected":
        frappe.db.sql("""UPDATE `tabTravel Request` SET `travel_status`=%s, `status`=%s where `name`=%s""", ("Completed","Completed", doc.travel_request_reference))
        frappe.db.commit()




