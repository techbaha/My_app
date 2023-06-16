// Copyright (c) 2023, baha and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bank Loan', {
	// refresh: function(frm) {

	// }
	repayment_months : function(frm){calculate(frm)},
	loan_amount : function(frm){calculate(frm)},
	interest : function(frm){calculate(frm)},
	
});

function calculate(frm){

if (frm.doc.loan_amount && frm.doc.repayment_months){
			var monthly=(frm.doc.loan_amount/ frm.doc.repayment_months);
			var monthly = monthly+monthly*frm.doc.interest/100;
			frm.doc.monthly_repayment=monthly;
			refresh_field("monthly_repayment");
		}else{
		frm.doc.monthly_repayment=0;
			refresh_field("monthly_repayment");
	}

}
