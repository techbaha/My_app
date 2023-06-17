// Copyright (c) 2023, baha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bank Loans"] = {
	"filters": [
		{fieldname:"company",label:__("Company"),fieldtype:"Link",options:"Company",default:frappe.defaults.get_user_default("Company"),reqd:1},
		{fieldname:"from_date",label:__("From Date"),fieldtype:"Date",default:frappe.defaults.get_user_default("year_start_date")},
		{fieldname:"to_date",label:__("To Date"),fieldtype:"Date",default:frappe.defaults.get_user_default("year_end_date")},

	]
};
