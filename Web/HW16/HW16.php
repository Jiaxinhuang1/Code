<!DOCTYPE html>
<html lang = "en">

<head>
	<title>HW16</title>
	<meta charset="UTF-8">
   	<meta name="description" content="Accessing Student Records Database">
   	<meta name="author" content="Jiaxin Huang">
   	<link href="HW16.css" rel="stylesheet">
</head>

<body>
	<form id = "login" method = "POST" action = "HW16.php">
		<div> <h1> Login to Database Actions </h1> </div>
		<table>
			<tr>
				<td> Username: </td>
				<td> <input type = "text" name = "username" required> </td>
			</tr>
			<tr>
				<td> Password: </td>
				<td> <input type = "password" name = "password" required> </td>
			</tr>
			<tr>
				<td> <input type = "submit" value = "Login" class = "button"> </td>
				<td> <input type = "reset" value = "Reset" class = "button"> </td>
			</tr>
			
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
	session_start();
	$username = $_POST['username'];
	$password = $_POST['password'];
	$login = false;

	$file = fopen("passwd.txt", "r");
	$file_array = file("passwd.txt");
	foreach ($file_array as $user) {
		$users[] = explode(":", $user);
	}
	fclose($file);
	
	foreach ($users as $user) {
		if ($username == trim($user[0]) && $password == trim($user[1])) {
			$_SESSION["username"] = $username;
			$login = true;
			header("Location: HW16Action.php");
		}
	}
	if (!$login) {
		echo "<tr><td colspan='2' style='color:darkred'> Login Failed </td></tr>";
	}
}
?>
		</table>
		
	</form>
</body>
</html>

