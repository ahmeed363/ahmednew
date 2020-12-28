# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ahmednew"
app_title = "ahmedNew"
app_publisher = "ahmed"
app_description = "ahmedNew"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "d"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ahmednew/css/ahmednew.css"
# app_include_js = "/assets/ahmednew/js/ahmednew.js"

# include js, css files in header of web template
# web_include_css = "/assets/ahmednew/css/ahmednew.css"
# web_include_js = "/assets/ahmednew/js/ahmednew.js"

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

# Website user home page (by function)
# get_website_user_home_page = "ahmednew.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ahmednew.install.before_install"
# after_install = "ahmednew.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ahmednew.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ahmednew.tasks.all"
# 	],
# 	"daily": [
# 		"ahmednew.tasks.daily"
# 	],
# 	"hourly": [
# 		"ahmednew.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ahmednew.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ahmednew.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ahmednew.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ahmednew.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ahmednew.task.get_dashboard_data"
# }

