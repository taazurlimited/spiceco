import frappe
from erpnext.controllers.accounts_controller import AccountsController
from erpnext.hr.doctype.loan.loan import Loan
from frappe.utils import flt, rounded, add_months, nowdate, getdate
@frappe.whitelist()
def validate(applicant,loan_amount):
    base_salary=frappe.get_list("Salary Structure Assignment", filters={'employee': applicant}, fields=['base'])
    if len(base_salary):
        if float(loan_amount) > base_salary[0].base:
            return 1
        else:
            return 0
    else:
        return 0

@frappe.whitelist()
def update_repayment_sched(name,rp,rsd):
    doc=frappe.get_doc("Loan",{'name':name})
    if not len(doc.repayment_schedule):
        doc.repayment_periods=int(rp)
        doc.repayment_start_date=rsd
        frappe.db.sql("""Delete from `tabRepayment Schedule` where parent=%s""",(name))
        doc.validate()
        
        count=1
        
        for i in doc.repayment_schedule:
            new_rp=frappe.get_doc({
                "doctype": "Repayment Schedule",
                "payment_date":i.payment_date,
                "principal_amount": i.principal_amount,
                "interest_amount": i.interest_amount,
                "total_payment": i.total_payment,
                "balance_loan_amount": i.balance_loan_amount,
                "paid": i.paid,
                "parent": name,
                "parentfield": "repayment_schedule",
                "parenttype": "Loan",
                "idx": count
                })
            count+=1
            new_rp.save()
            new_rp1=frappe.get_doc({
                "doctype": "Loan Repayment Schedule",
                "payment_date1":i.payment_date,
                "principal_amount1": i.principal_amount,
                "interest_amount1": i.interest_amount,
                "total_payment1": i.total_payment,
                "balance_loan_amount1": i.balance_loan_amount,
                "paid1": i.paid,
                "parent": name,
                "parentfield": "loan_repayment_schedule",
                "parenttype": "Loan",
                "idx": count,
                "source": new_rp.name
                })
            count+=1
            new_rp1.save()
            # doc.source=new_rp.name
            # doc.save()
    

@frappe.whitelist()
def generate_data_for_lrs(name):
    
    frappe.db.sql("""Delete from `tabLoan Repayment Schedule` where parent=%s""",(name))
    repayment_schedule=frappe.db.sql("""Select payment_date,principal_amount,interest_amount,total_payment,balance_loan_amount,paid,name,idx from `tabRepayment Schedule` where parent=%s""",(name))
    for i in repayment_schedule:
        new_rp=frappe.get_doc({
            "doctype": "Loan Repayment Schedule",
            "payment_date1":i[0],
            "principal_amount1": i[1],
            "interest_amount1": i[2],
            "total_payment1": i[3],
            "balance_loan_amount1": i[4],
            "paid1": i[5],
            "source": i[6],
            "parent": name,
            "parentfield": "loan_repayment_schedule",
            "parenttype": "Loan",
            "idx": i[7]
            })
        new_rp.save()
    return 0
            
@frappe.whitelist()
def set_repayment_schedule(name,source,parent,payment_date):
    loan_repayment_schedule=frappe.db.sql("""Select payment_date1,principal_amount1,interest_amount1,total_payment1,balance_loan_amount1,paid1,idx,source from `tabLoan Repayment Schedule` where name=%s""",(name))
    frappe.db.sql("""Update `tabLoan` set docstatus=0 where name=%s""",(parent))
    # frappe.db.sql("""Delete from `tabRepayment Schedule` where name=%s""",(source))
    # for i in loan_repayment_schedule:
    #     new_rp=frappe.get_doc({
    #                 "doctype": "Repayment Schedule",
    #                 "payment_date":payment_date,
    #                 "principal_amount": i[1],
    #                 "interest_amount": i[2],
    #                 "total_payment": i[3],
    #                 "balance_loan_amount": i[4],
    #                 "paid": i[5],
    #                 "parent": parent,
    #                 "parentfield": "repayment_schedule",
    #                 "parenttype": "Loan",
    #                 "idx": i[6]
    #                 })
    #     new_rp.save()
    #     # return new_rp.name
    #     frappe.db.sql("""Update `tabLoan Repayment Schedule` set source=%s,payment_date1=%s where name=%s""",(new_rp.name,payment_date,name))
    #     return new_rp.name