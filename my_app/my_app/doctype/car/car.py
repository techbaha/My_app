# Copyright (c) 2023, baha and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Car(Document):

	def before_save(self):
		self.validate()




	def validate(self):
		carplate=self.carplate
		if len(carplate)!=8:
			frappe.throw(_("Carplate must be in format abcd-123"))
		if carplate[4]!="-"  or carplate[:4].isalpha()==False or carplate[5:].isnumeric()==False :
			frappe.throw(_("Carplate must be in format abcd-123"))
