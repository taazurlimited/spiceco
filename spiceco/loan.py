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
    print(doc.repayment_periods)
    print(rp)
    print(doc.repayment_start_date)
    print(rsd)
    if doc.repayment_periods!=int(rp) or str(doc.repayment_start_date)!=rsd:
        doc.repayment_periods=int(rp)
        doc.repayment_start_date=rsd
        frappe.db.sql("""Update `tabLoan` set repayment_periods=%s,repayment_start_date=%s where name=%s""",(int(rp),rsd,name))
        frappe.db.sql("""Delete from `tabRepayment Schedule` where parent=%s""",(name))
        frappe.db.sql("""Delete from `tabLoan Repayment Schedule` where parent=%s""",(name))
        
        
        doc.validate()
        doc.make_repayment_schedule()
        
        count=1
        print(doc.repayment_schedule)
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
def generate_data_for_lrs(name,rp,rsd):
    
    frappe.db.sql("""Delete from `tabLoan Repayment Schedule` where parent=%s""",(name))
    repayment_schedule=frappe.get_doc("Loan",{'name':name})
    
    if repayment_schedule.repayment_periods!=int(rp) or str(repayment_schedule.repayment_start_date)!=rsd:
        repayment_schedule.make_repayment_schedule()
        repayment_schedule.validate()
        repayment_schedule.save()
    # repayment_schedule=frappe.db.sql("""Select payment_date,principal_amount,interest_amount,total_payment,balance_loan_amount,paid,name,idx from `tabRepayment Schedule` where parent=%s""",(name))
    for i in repayment_schedule.repayment_schedule:
        new_rp=frappe.get_doc({
            "doctype": "Loan Repayment Schedule",
            "payment_date1":i.payment_date,
            "principal_amount1": i.principal_amount,
            "interest_amount1": i.interest_amount,
            "total_payment1": i.total_payment,
            "balance_loan_amount1": i.balance_loan_amount,
            "paid1": i.paid,
            "source": i.name,
            "parent": name,
            "parentfield": "loan_repayment_schedule",
            "parenttype": "Loan",
            "idx": i.idx
            })
        new_rp.save()
    return 0
            
@frappe.whitelist()
def set_repayment_schedule(parent):
    frappe.db.sql("""Update `tabLoan` set docstatus=%s where name=%s""",(parent))
   

@frappe.whitelist()
def check_if_loan_deduction_started(start_date,name):
    salary_slips=frappe.db.sql("""Select name from `tabSalary Slip` where start_date <= %s and end_date>=%s""",(start_date,start_date))
    for i in salary_slips:
        for ii in frappe.get_list("Salary Slip Loan",filters={'parent':i[0]}):
            return 1
    return 0
    

@frappe.whitelist()
def check_loan_schedule(name):
    loans=frappe.get_list("Loan Repayment Schedule",filters={'name':name},fields=['payment_date1'])
    cannot_be_changed=0
    for i in loans:
        salary_slips=frappe.db.sql("""Select name from `tabSalary Slip` where start_date <= %s and end_date>=%s""",(i['payment_date1'],i['payment_date1']))
        if len(salary_slips)>0:
            cannot_be_changed=i['payment_date1']
    return cannot_be_changed   