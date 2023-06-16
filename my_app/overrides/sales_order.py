from erpnext.selling.doctype.sales_order.sales_order import SalesOrder
import frappe
from frappe import _
from frappe.utils import getdate,date_diff





class CustomSalesOrder(SalesOrder):
	

	def before_save(self):
		now=getdate()
		diff=date_diff(self.delivery_date,now)
		self.days_till_delivery=diff


def update_days_of_delivery():
	order=frappe.db.get_list("Sales Order",filters=[["status","in",["Draft","To Deliver","To Deliver and Bill"]]],fields=["name","delivery_date","status","days_till_delivery"])
	now=getdate()
	for o in order:
		diff=date_diff(o["delivery_date"],now)
		frappe.db.set_value("Sales Order",o["name"],"days_till_delivery",diff,update_modified=False)
	frappe.db.commit()
