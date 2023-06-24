<!DOCTYPE html>
<html lang = "en">

<head>
	<title>HW15</title>
	<meta charset="UTF-8">
   	<meta name="description" content="Self Grading Quiz Using Sessions">
   	<meta name="author" content="Jiaxin Huang">
   	<link href="HW15.css" rel="stylesheet">
</head>

<body>
	<form id = "login" method = "POST" action = "HW15.php">
		<div> <h1> Login to Start Quiz </h1> </div>
		<table>
			<tr>
				<td> Username: </td>
				<td> <input type = "text" name = "username"> </td>
			</tr>
			<tr>
				<td> Password: </td>
				<td> <input type = "password" name = "password"> </td>
			</tr>
			<tr>
				<td> <input type = "submit" value = "Login" class = "button"> </td>
				<td> <input type = "reset" value = "Clear" class = "button"> </td>
			</tr>
			
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
	session_start();
	$username = $_POST['username'];
	$password = $_POST['password'];
	$login = false;
	$repeat = false;

	$file = fopen("329E.passwd.txt", "r");
	$file_array = file("329E.passwd.txt");
	foreach ($file_array as $user) {
		$users[] = explode(":", $user);
	}
	fclose($file);

	$results = fopen("results.txt", "r");
	$results_array = file("results.txt");
	foreach ($results_array as $r) {
		$results_list[] = explode(":", $r);
	}

	fclose($results);

	//print_r ($users);
	//print_r($results_list);
	
	foreach ($users as $user) {
		if ($username == trim($user[0]) && $password == trim($user[1])) {
			foreach ($results_list as $result) {
				if ($username == trim($result[0])) {
					$repeated = true;
					break;
				}
			}
			if (!$repeated) {
				$_SESSION["username"] = $username;
				$_SESSION["score"] = 0;
				$login = true;
				header("Location: HW15Quiz.php");
			}
			else {
				echo "<tr><td colspan='2' style='color:darkred'> You Have Already Taken the Quiz </td></tr>";

			}
		}
	}
	if (!$login && !$repeated) {
		echo "<tr><td colspan='2' style='color:darkred'> Incorrect Username or Password </td></tr>";
	}
}
?>
		</table>
		
	</form>
</body>
</html>

