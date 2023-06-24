function Validate() {
	var username = document.RegistrationForm.username.value
	var password = document.RegistrationForm.password.value
	var repeat_pass = document.RegistrationForm.repeat_pass.value
	var isUsernameCorrect = false
	var isPasswordCorrect = true
	var isPassEqual = false

	// check if the username is valid
	if ((username.length >= 6 && username.length <= 10)
		&& (isLetterDigit(username))
		&& (!(username.charCodeAt(0) > 47 && username.charCodeAt(0) < 58)))
	{
		isUsernameCorrect = true
	}
	else {
		isUsernameCorrect = false
	}

	//check if the password and reset password match
	if (password === repeat_pass){
		isPassEqual = true
	}
	else {
		isPassEqual = false
	}

	// check if the password is valid
	if ((password.length >= 6 && password.length <= 10)
		&& (isLetterDigit(password))
		&& (passwordLimit(password))) {
		isPasswordCorrect = true
	}
	else {
		isPasswordCorrect = false
	}

	// check to see if both username and password is valid and reset_pass equals to password
	if (isUsernameCorrect && isPasswordCorrect && isPassEqual){
		alert("User Validated")
	}
	else {
		alert("Invalid Username or Password")
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