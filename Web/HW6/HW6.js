function Calculate() {
	// inititalize the variables
	var principal_amt = document.MortageForm.principal_amt.value
	var interest_rate = document.MortageForm.interest_rate.value
	var loan_term = document.MortageForm.loan_term.value
	
	// alert the user if non-numeric values or negative numbers are entered
	if (principal_amt <= 0 || isNaN(principal_amt)) {
		alert(principal_amt + " is not a valid input. Please enter a valid principal amount")
		document.MortageForm.principal_amt.value = ""
	}
	else if (interest_rate <= 0 || isNaN(interest_rate) || interest_rate >= 1) {
		alert(interest_rate + " is not a valid input. Please enter a valid interest rate")
		document.MortageForm.interest_rate.value = ""
	}
	else if (loan_term <=0 || isNaN(loan_term) || parseInt(loan_term) != loan_term) {
		alert(loan_term + " is not a valid input. Please enter a valid loan term in months")
		document.MortageForm.loan_term.value = ""
	}
	else {
		// formula for monthly payment is R = P*r/(1-(1/(1+r)^n))
		var P = parseFloat(principal_amt)
		var r = parseFloat(interest_rate)/12
		var n = parseInt(loan_term)
		var monthly_payment = (P*r/(1-(1/(Math.pow((1+r), n))))).toFixed(2)
		var sum_payment = (monthly_payment * n).toFixed(2)
		var total_interest = (sum_payment - principal_amt).toFixed(2)

		// display the result on the output section
		month_pay_text = document.getElementById("monthly payment")
		month_pay_text.innerHTML = "$ " + monthly_payment
		sum_pay_text = document.getElementById("sum payment")
		sum_pay_text.innerHTML = "$ " + sum_payment
		total_interest_text = document.getElementById("total interest")
		total_interest_text.innerHTML = "$ " + total_interest
	}
}