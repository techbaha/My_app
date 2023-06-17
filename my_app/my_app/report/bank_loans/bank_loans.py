# Copyright (c) 2023, baha and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns=get_columns(filters=filters)
	banks=frappe.db.get_list("Bank Person")
	total_loans_list=[]
	total_outstanding_list=[]
	total_interest=0
	for b in banks:
		d={"bank":b["name"]}
		total_loans=0
		total_repayments=0
		interest=0
		if "from_date" in filters.keys() and "to_date" in filters.keys():
			loans=frappe.db.get_list("Bank Loan",filters=[["bank_name","in",[b["name"]]],["posting_date","between",[filters["from_date"],filters["to_date"]]]])
		else:
			loans=frappe.db.get_list("Bank Loan",filters={"bank_name":b["name"]})
		for l in loans:
			loan=frappe.get_doc("Bank Loan",l["name"])
			total_loans+=loan.loan_amount
			interest+=loan.loan_amount*loan.interest/100
			for s in loan.schedule:
				if s.journal_entry:
					total_repayments+=s.total_payment

		d["total_repayments"]=round(total_repayments,2)
		d["total_loans"]=total_loans
		total_loans_list.append(total_loans)
		d["interest"]=interest
		total_interest+=interest
		d["outstanding_amount"]=round(total_loans+interest-total_repayments,2)
		total_outstanding_list.append(round(total_loans+interest-total_repayments,2))
		data.append(d)		
	banks=[b["name"] for b in banks]
	chart={"data":{"labels":banks,"datasets":[{"name":"Total Loans","values":total_loans_list},{"name":"Total Outstanding","values":total_outstanding_list}]} , "type":"bar"}
	cards=[{"label":"Total Loans","value":"{:,.2f} SAR".format(sum(total_loans_list)),"indicator":"green"},{"label":"Total Interest","value":"{:,.2f} SAR".format(total_interest),"indicator":"blue"},{"label":"Total Outstanding","value":"{:,.2f} SAR".format(sum(total_outstanding_list)),"indicator":"red"}]
	return columns, data , None, chart, cards






def get_columns(filters=None):
	columns=[
		{"fieldname":"bank","label":_("Bank"),"fieldtype":"Link","options":"Bank Loan"},
		{"fieldname":"total_loans","label":_("Total Loans"),"fieldtype":"Currency"},
		{"fieldname":"interest","label":_("Total Interest"),"fieldtype":"Currency"},
		{"fieldname":"total_repayments","label":_("Total repayments"),"fieldtype":"Currency"},
		{"fieldname":"outstanding_amount","label":_("Outstanding Amount"),"fieldtype":"Currency"}
	]
	return columns
