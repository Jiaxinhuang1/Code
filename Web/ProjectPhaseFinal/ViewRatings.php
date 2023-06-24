<?php
	session_start();
	error_reporting(E_ALL);
	ini_set("display_errors", "on");
	$server = 'spring-2022.cs.utexas.edu';
  	$user = 'cs329e_bulko_mka72';
  	$pwd = 'Fatal5Tune6pride';
  	$dbName = 'cs329e_bulko_mka72';
	
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
	$courseName = $_GET["courseName"];
	$rating = $_GET["rating"];
	$comment = $_GET["comment"];
	$sort = $_COOKIE["Sort"];
	
	// Escape User Input to help prevent SQL injection
	$courseName = $mysqli->real_escape_string($courseName);
	$rating = $mysqli->real_escape_string($rating);
	$comment = $mysqli->real_escape_string($comment);

	// Build Query
	//echo "<code>... Building query</code><br>";
	
	if ($sort == "None") {
		$query = "SELECT * FROM ratings";
	}
	elseif ($sort == "Name") {
		$query = "SELECT * FROM ratings ORDER BY courseName";
	}
	elseif ($sort == "Rating") {
		$query = "SELECT * FROM ratings ORDER BY rating";
	}
	
	
	// Execute Query
	//echo "<code>... Executing query</code><br>";
	$result = $mysqli->query($query) or die($mysqli->error);

	// Build Result String
	$display_string = "<table id = 'RatingsResult'><caption><strong>Rating Results</strong></caption>
<tr><th>Couse Name</th><th>Rating</th><th>Comments</th></tr>";
	//$row = $result->fetch_array(MYSQLI_ASSOC)
	// Insert new row in table for each student returned
	if (!mysqli_num_rows($result)) {
		$display_string = "<h4 style='text-align: center'>No Matches</h4>";
	}
	else {
		while ($row = $result->fetch_array(MYSQLI_ASSOC)) {
			$display_string .= "<tr>";
			$display_string .= "<td>$row[courseName]</td>";
			$display_string .= "<td>$row[rating]</td>";
			$display_string .= "<td>$row[comment]</td>";
			$display_string .= "</tr>";
		}
		$display_string .= "</table>";
	}
	//echo "Query: <code>". $query . "</code> <br><br>";
	echo $display_string;
?>