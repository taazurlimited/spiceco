# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "spiceco"
app_title = "spiceco"
app_publisher = "kkulloters"
app_description = "spiceco"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vanessa.bualat01@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/spiceco/css/spiceco.css"
# app_include_js = "/assets/spiceco/js/spiceco.js"

# include js, css files in header of web template
# web_include_css = "/assets/spiceco/css/spiceco.css"
# web_include_js = "/assets/spiceco/js/spiceco.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Expense Claim Type": "public/js/script_for_expense_claim_type.js",
    "Expense Claim": "public/js/script_for_expense_claim.js",
    "Travel Request": "public/js/script_for_travel_request.js",
    "Loan Application": "public/js/script_for_loan_application.js",
    "Loan": "public/js/script_for_loan.js",
    "Salary Slip": "public/js/script_for_salary_slip.js",
    #"Travel Request": "public/js/travel_request_list.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "spiceco.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "spiceco.install.before_install"
# after_install = "spiceco.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "spiceco.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Travel Request": {
		"on_submit": "spiceco.doc_events.submit_tr"
	},
    "Expense Claim": {
		"on_submit": "spiceco.doc_events.submit_expense"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"spiceco.tasks.all"
# 	],
# 	"daily": [
# 		"spiceco.tasks.daily"
# 	],
# 	"hourly": [
# 		"spiceco.tasks.hourly"
# 	],
# 	"weekly": [
# 		"spiceco.tasks.weekly"
# 	]
# 	"monthly": [
# 		"spiceco.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "spiceco.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "spiceco.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "spiceco.task.get_dashboard_data"
# }
#hooks
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                ['Expense Claim Detail-cost_center', 'Expense Claim Type-deferred_expense_account',
                 'Travel Request-status', 'Travel Request-advance_amount', 'Travel Request-travel_approver',
                 'Travel Request-travel_status', "Expense Claim-travel_request_reference", "Department-travel_approver",
                 "Department-travel_approvers", "Employee Advance-travel_request", "Travel Request-approval_status", "Loan Type-no_additional_loan_allowed","HR Settings-leave_without_pay",
                 "Loan-loan_repayment_period_in_months", "Loan-loan_repayment_start_date","Loan-loan_repayment_schedule"]

            ]
        ]
    }
]

