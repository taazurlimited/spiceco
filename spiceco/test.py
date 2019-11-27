import frappe

def t():
	s=frappe.get_list("Account", filters={'name':'Cash - ba'}, fields=['account_currency'])
	print(s)
