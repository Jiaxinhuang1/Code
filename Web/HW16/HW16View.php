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
	$lastName = $_GET['lastName'];
	$firstName = $_GET['firstName'];
	$id = $_GET['id'];
	
	//$Choice = $_GET["choice"];
	//echo $Choice;
	//$ViewAll = $_POST['showAll'];

	// Escape User Input to help prevent SQL injection
	$lastName = $mysqli->real_escape_string($lastName);
	$firstName = $mysqli->real_escape_string($firstName);

	// Build Query
	//echo "<code>... Building query</code><br>";
	
	if ($lastName == "" && $firstName == "" && $id == "") {
		$query = "SELECT * FROM students ORDER BY lastName, firstName";
	}
	elseif ($id != "" && $lastName == "" && $firstName == "") {
		$query = "SELECT * FROM students WHERE id = '$id'";
	}
	elseif ($id != "" && $lastName != "" && $firstName == "") {
		$query = "SELECT * FROM students WHERE lastName = '$lastName' AND id = '$id'";
	}
	elseif ($id != "" && $lastName == "" && $firstName != "") {
		$query = "SELECT * FROM students WHERE firstName = '$firstName' AND id = '$id'";
	}
	elseif ($id == "" && $lastName != "" && $firstName == "") {
		$query = "SELECT * FROM students WHERE lastName = '$lastName'";
	}
	elseif ($id == "" && $lastName != "" && $firstName != "") {
		$query = "SELECT * FROM students WHERE (lastName = '$lastName') AND (firstName = '$firstName')";
	}
	elseif ($id == "" && $lastName == "" && $firstName != "") {
		$query = "SELECT * FROM students WHERE firstName = '$firstName'";
	}
	elseif ($id != "" && $lastName != "" && $firstName != "") {
		$query = "SELECT * FROM students WHERE (id = '$id') AND (lastName = '$lastName') AND (firstName = '$firstName')";
	}
	
	
	// Execute Query
	//echo "<code>... Executing query</code><br>";
	$result = $mysqli->query($query) or die($mysqli->error);

	// Build Result String
	$display_string = "<table border=2> <tr> <th>ID</th><th>Last Name</th><th>First Name</th><th>Major</th><th>GPA</th></tr>";
	//$row = $result->fetch_array(MYSQLI_ASSOC)
	// Insert new row in table for each student returned
	if (!mysqli_num_rows($result)) {
		$display_string = "<h4 style='text-align: center'>No Matches</h4>";
	}
	else {
		while ($row = $result->fetch_array(MYSQLI_ASSOC)) {
			$display_string .= "<tr>";
			$display_string .= "<td>$row[id]</td>";
			$display_string .= "<td>$row[lastName]</td>";
			$display_string .= "<td>$row[firstName]</td>";
			$display_string .= "<td>$row[major]</td>";
			$display_string .= "<td>$row[gpa]</td>";
			$display_string .= "</tr>";
		}
		$display_string .= "</table>";
	}
	echo "Query: <code>". $query . "</code> <br><br>";
	echo $display_string;
?>