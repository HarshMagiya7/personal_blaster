from . import __version__ as app_version

app_name = "personal_blaster"
app_title = "Personal Blaster"
app_publisher = "Novacept"
app_description = "Campaigning app for Whatsapp, Email and SMS"
app_email = "info@novacept.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/personal_blaster/css/personal_blaster.css"
# app_include_js = "/assets/personal_blaster/js/personal_blaster.js"

# include js, css files in header of web template
# web_include_css = "/assets/personal_blaster/css/personal_blaster.css"
# web_include_js = "/assets/personal_blaster/js/personal_blaster.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "personal_blaster/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "personal_blaster.utils.jinja_methods",
#	"filters": "personal_blaster.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "personal_blaster.install.before_install"
# after_install = "personal_blaster.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "personal_blaster.uninstall.before_uninstall"
# after_uninstall = "personal_blaster.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "personal_blaster.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
#		"personal_blaster.tasks.all"
#		"personal_blaster.personal_blaster.doctype.social_post.social_post.process_scheduled_social_media_posts",
		"personal_blaster.personal_blaster.doctype.email_post.email_post.send_email_to_leads_or_contacts",
		"personal_blaster.personal_blaster.doctype.whatsapp_post.whatsapp_post.process_scheduled_whatsapp_message",
		"personal_blaster.personal_blaster.doctype.client.client.upload_all_contacts",
		"personal_blaster.personal_blaster.doctype.email_post.email_post.set_email_campaign_status"
	],
#}
#	"daily": [
#		"personal_blaster.tasks.daily"
#	],
	"hourly": [
		"personal_blaster.personal_blaster.doctype.client.client.update_all_client"
	],
#	"weekly": [
#		"personal_blaster.tasks.weekly"
#	],
#	"monthly": [
#		"personal_blaster.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "personal_blaster.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "personal_blaster.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "personal_blaster.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"personal_blaster.auth.validate"
# ]
