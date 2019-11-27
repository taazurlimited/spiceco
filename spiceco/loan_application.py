import frappe

@frappe.whitelist()
def validate_submission(applicant,loan_type):
    return len(frappe.get_list("Loan", filters={'applicant':applicant,'loan_type':loan_type}, fields=['name']))