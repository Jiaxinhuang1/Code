<!DOCTYPE html>
<html lang = "en">

<head>
	<title>HW17</title>
	<meta charset="UTF-8">
   	<meta name="description" content="User Registration with AJAX and SQL Database">
   	<meta name="author" content="Jiaxin Huang">
   	<link href="HW17.css" rel="stylesheet">
</head>

<body>
	<form id = "login" method = "POST" action = "HW17.php">
		<script>
			function ajaxFunction(server, user, pwd, dbName) {
				var ajaxRequest
				ajaxRequest = new XMLHttpRequest()
				ajaxRequest.onreadystatechange = function () {
					if (ajaxRequest.readyState == 4) {
						var ajaxDisplay = document.getElementById("ajaxDiv")
						ajaxDisplay.innerHTML = ajaxRequest.responseText
					}
				}
				var username = document.getElementById("username").value
				var password = document.getElementById("password").value
				var queryString = "?username=" + username + "&password=" + password + "&server=" + server + "&user=" + user + "&pwd=" + pwd + "&dbName=" + dbName
				ajaxRequest.open("GET", "HW17Action.php" + queryString, true)
				ajaxRequest.send(null);
			}
		</script>
		<div> <h1> User Login </h1> </div>
		<table>
			<tr>
				<td> Username: </td>
				<td> <input id = "username" type = "text" name = "username" required> </td>
			</tr>
			<tr>
				<td> Password: </td>
				<td> <input id = "password" type = "password" name = "password" required> </td>
			</tr>
			<tr>
				<td> <input type = "button" value = "Login" onclick = "ajaxFunction('spring-2022.cs.utexas.edu','cs329e_bulko_jiaxin','knock8severe_longer','cs329e_bulko_jiaxin')"class = "button"> </td>
				<td> <input type = "reset" value = "Reset" class = "button"> </td>
			</tr>
		<tr>
			<td colspan = "2" id = "ajaxDiv" style="text-align: center; color:darkred"></td>
		</tr>
		</table>
		
	</form>
</body>
</html>

