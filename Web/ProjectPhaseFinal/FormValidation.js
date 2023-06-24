function Validate() {
	var username = document.RegistrationForm.user.value
	var password = document.RegistrationForm.pwd.value
	var repeat_pass = document.RegistrationForm.confirmpwd.value
	var form = document.getElementById("LoginForm")
	var isUsernameCorrect = false
	var isPasswordCorrect = true
	var isPassEqual = false

	// check if the username is valid
	if (username.length >= 6 && username.length <= 10)
	{
		isUsernameCorrect = true
	}
	else {
		alert("Username needs to be between 6-10 characters")
		isUsernameCorrect = false
	}

	//check if the password and reset password match
	if (password === repeat_pass){
		isPassEqual = true
	}
	else {
		alert("Password does not match")
		isPassEqual = false
	}

	// check if the password is valid
	if (password.length >= 6 && password.length <= 10) {
		isPasswordCorrect = true
	}
	else {
		alert("Password needs to be between 6-10 characters")
		isPasswordCorrect = false
	}

	// check to see if both username and password is valid and reset_pass equals to password
	if (isUsernameCorrect && isPasswordCorrect && isPassEqual){
		document.getElementById("RegisterBtn").type = "submit"
	}
	else {
		alert("Failed to Register")
	}
}

// Helper function to see if the string is a number or digit
function isLetterDigit(string){
	var value = 0
	for (i = 0; i < string.length; i++){
		// find ascii value of each char and return false if not in number or digit range
		value = string.charCodeAt(i)
		if ((value < 48) || (value > 57 && value < 65) || (value > 90 && value < 97) || (value > 122)) {
			return false
		}
	}
	return true
}

// Helper function to see if there is at least one upper, lower, and digit in string
function passwordLimit(string){
	var value = 0
	var lower = false
	var upper = false
	var digit = false
	for (i = 0; i < string.length; i++) {
		value = string.charCodeAt(i)
		if (value > 47 && value < 58){
			digit = true
		}
		else if (value > 64 && value < 91) {
			upper = true
		}
		else if (value > 96 && value < 123) {
			lower = true
		}
		if (digit && upper && lower) {
			return true
		}
	}
	return false
}