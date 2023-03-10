# Copyright (c) 2022, Novacept and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
class ClientGroup(Document):

	def validate(self):
		if not self.interest and not self.city and not self.country:
			frappe.throw(_('All fields cannot be empty'))

	@frappe.whitelist()
	def filter(self):
		city_list = {}
		interest_list = {}
		country_list = {}

		filter_list = []

		if self.interest:

			interests = frappe.db.get_list('Client',fields=['name','`tabInterests`.`Interest`'],as_list=1)
			in_list = []
			for i in interests:
				in_list.append(list(i))
			interest_list = []
			for i in in_list:
				if i[1] == self.interest:
					value = []
					value.append(i[0])
					interest_list.append(tuple(value))
			interest_list = tuple(interest_list)
			filter_list.append(set(interest_list))

		if self.city:
			city_list = frappe.db.get_list('Client',filters={'City':self.city},as_list=1)
			filter_list.append(set(city_list))
		if self.country:
			country_list = frappe.db.get_list('Client',filters={'Country':self.country},as_list=1)
			filter_list.append(set(country_list))
#		filter_list = [set(city_list),set(interest_list),set(country_list)]
		non_empty_list = [x for x in filter_list]
		print(non_empty_list)
		if not non_empty_list:
			frappe.throw((f'No contacts added'))
			return
		final_list = set.intersection(*non_empty_list)
		print(final_list)
		for i in final_list:
			self.append("clients",{"client_member":i[0]})
			print(i[0])
		self.save()
		frappe.msgprint((f'{len(final_list)} contacts added'))
