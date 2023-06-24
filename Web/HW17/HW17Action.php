<?php
	error_reporting(E_ALL);
	ini_set("display_errors", "on");
	$server = 'spring-2022.cs.utexas.edu';
	$user = 'cs329e_bulko_jiaxin';
	$pwd = 'knock8severe_longer';
	$dbName = 'cs329e_bulko_jiaxin';
	
	// Connect to MySQL Server
	$mysqli = new mysqli($server, $user, $pwd, $dbName);
	if ($mysqli->connect_errno) {
		die('Connect Error: ' . $mysqli->connect_errno . ': ' . $mysqli->connect_error);
	}
	else {
		//echo "<code>...Connecting successful</code><br>";
	}

	// Select Database
	$mysqli->select_db($dbName) or die($mysqli->error);

	// Retrieve data from Query String
	$username = $_GET['username'];
	$password = $_GET['password'];
	
	// Escape User Input to help prevent SQL injection
	$username = $mysqli->real_escape_string($username);
	$password = $mysqli->real_escape_string($password);
	//echo $username;
	//echo $password;


	// Build Query
	//echo "<code>... Building query</code><br>";
	
	$query = "SELECT * FROM passwords WHERE username = '$username'";
		
	// Execute Query
	//echo "<code>... Executing query</code><br>";
	$result = $mysqli->query($query) or die($mysqli->error);
	//$row = mysqli_fetch_array($result, MYSQLI_ASSOC);

	$querySpecific = "SELECT * FROM passwords WHERE username = '$username' AND password = '$password'";
	$resultSpecific = $mysqli->query($querySpecific) or die($mysqli->error);
	

	// Build Result String
	if (!mysqli_num_rows($result)) {
		$queryCommand = "INSERT INTO passwords VALUES ('$username', '$password')";
		if ($mysqli->query($queryCommand) === TRUE) { 
			$display_string = "New User Registered";
		}
	}
	elseif (mysqli_num_rows($result) >= 1) {
		if (mysqli_num_rows($resultSpecific) >= 1) {
			$display_string = "User and Password Confirmed";
		}
		else {
			$queryCommand = "UPDATE passwords SET password = '$password' WHERE username = '$username'";
			if ($mysqli->query($queryCommand) === TRUE) { 
				$display_string = "Password Changed";
			}
		}
	}

	//echo "Query: <code>". $query . "</code> <br><br>";
	echo $display_string;
?>