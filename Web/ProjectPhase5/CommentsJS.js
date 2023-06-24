function validate()
{
	console.log("submitted");
	var name = document.forms["Comments"]["name"].value;
	var email = document.forms["Comments"]["email"].value;
	if(name.length == 0 || email.length == 0){
		alert("Name and Email cannot be blank");  
	}
	else {
		alert("Form Submitted");
	}
}