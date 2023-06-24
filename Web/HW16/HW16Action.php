<?php 

 if ($_POST["page"] == "Insert Student Record" || $_POST["page"] == "Insert")
 {
   DisplayInsert();
 }
 elseif ($_POST["page"] == "Update Student Record" || $_POST["page"] == "Update")
 {
   DisplayUpdate();
 }
 elseif ($_POST["page"] == "Delete Student Record" || $_POST["page"] == "Delete")
 {
   DisplayDelete();
 }
 elseif ($_POST["page"] == "View Student Record" || $_POST["page"] == "View")
 {
   DisplayView();
 }
 elseif ($_POST["page"] == "Logout")
 {
   DisplayLogout();
 }
 elseif ($_POST["page"] == "Back to Actions")
 {
   DisplayAction();
 }
 else
 {
    DisplayAction();
 }

 function DisplayAction()
 {
  $script = $_SERVER['PHP_SELF'];
  print <<<ACTION
  <html>
  <head>
  	<title> Action </title>
  	<link href="HW16.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "action" method = "post" action = "$script">
  	<h1> Actions </h1>
	<div id = actionBtnGroup>
		<input name = "page" type = "submit" value = "Insert Student Record" class = "actionBtn"/>
		<input name = "page" type = "submit" value = "Update Student Record" class = "actionBtn"/>	
		<input name = "page" type = "submit" value = "Delete Student Record" class = "actionBtn"/>
		<input name = "page" type = "submit" value = "View Student Record" class = "actionBtn"/>
		<input name = "page" type = "submit" value = "Logout" class = "actionBtn"/>
	</div>
  </form>
  </body>
  </html>
ACTION;
  }

 function DisplayInsert()
 {
  print <<<INSERT
  <html>
  <head>
  	<title> Action </title>
  	<link href="HW16.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "action" method = "post" action = "$script">
  	<h1> Insert Student Record </h1>
	<table>
		<tr>
			<td> ID: </td>
			<td> <input type = "number" name = "id" required> </td>
		</tr>
		<tr>
			<td> Last Name: </td>
			<td> <input type = "text" name = "lastName" required> </td>
		</tr>
		<tr>
			<td> First Name: </td>
			<td> <input type = "text" name = "firstName" required> </td>
		</tr>
		<tr>
			<td> Major: </td>
			<td> <input type = "text" name = "major" required> </td>
		</tr>
		<tr>
			<td> GPA: </td>
			<td> <input type = "number" name = "gpa" step = "0.01" required> </td>
		</tr>
		<tr>
			<td> <button class = "actionBtn" onclick="window.location.href = 'HW16Action.php value = "Back to Actions" formnovalidate>Go Back</button></td>
			<td> <input name = "page" type = "submit" value = "Insert" class = "actionBtn"/> </td>
		</tr>
	</table>
  	</form>
  </body>
  </html>
INSERT;
	if ($_POST["page"] == "Insert") {
		$id = $_POST['id'];
		$lastName = $_POST['lastName'];
		$firstName = $_POST['firstName'];
		$major = $_POST['major'];
		$gpa = $_POST['gpa'];

  		$server = 'spring-2022.cs.utexas.edu';
  		$user = 'cs329e_bulko_jiaxin';
  		$pwd = 'knock8severe_longer';
  		$dbName = 'cs329e_bulko_jiaxin';
		//echo $id . "<br>". $lastName."<br>".$firstName."<br>".$major."<br>".$gpa."<br>";


		$mysqli = new mysqli($server, $user, $pwd, $dbName);
		if ($mysqli->connect_errno) {
			die('Connect Error: ' . $mysqli->connect_errno . ': ' . $mysqli->connect_error);
		}
		else {
			//echo "<code>...Connecting successful</code><br>";
		}

		// Select Database
		$mysqli->select_db($dbName) or die($mysqli->error);
		//echo "<code>... Executing query</code><br>";
		$query = "INSERT INTO students VALUES ($id, '$lastName', '$firstName', '$major', $gpa)";
		//$result = $mysqli->query($query) or die($mysqli->error);
		if ($mysqli->query($query) === TRUE) {
			echo "<script>alert('SUCCESSFULLY INSERTED INTO DATABASE')</script>";
		}
		else {
			$error = $mysqli->error;
			echo "<script>alert('FAIL TO INSERT: Make Sure ID is Unique')</script>";
		}
		$mysqli->close();
	}

  }

 function DisplayUpdate()
 {
  print <<<UPDATE
  <html>
  <head>
  	<title> Action </title>
  	<link href="HW16.css" rel="stylesheet">
  </head>
  <body>
  	<form name = "Form" id = "Form" class = "action" method = "post" action = "$script">
	<h1> Update Student Record </h1>
	<table>
		<tr>
			<td> ID: </td>
			<td> <input type = "number" name = "id" required> </td>
		</tr>
		<tr>
			<td> Last Name: </td>
			<td> <input type = "text" name = "lastName"> </td>
		</tr>
		<tr>
			<td> First Name: </td>
			<td> <input type = "text" name = "firstName"> </td>
		</tr>
		<tr>
			<td> Major: </td>
			<td> <input type = "text" name = "major"> </td>
		</tr>
		<tr>
			<td> GPA: </td>
			<td> <input type = "number" name = "gpa" step = "0.01"> </td>
		</tr>
		<tr>
			<td> <button class = "actionBtn" onclick="window.location.href = 'HW16Action.php value = "Back to Actions" formnovalidate>Go Back</button></td>
			<td> <input name = "page" type = "button" value = "Update" onclick = "Validate()" class = "actionBtn"/> </td>
		</tr>
	</table>
	<script>
		function Validate() {
			var id = document.Form.id.value
			var lastName = document.Form.lastName.value
			var firstName = document.Form.firstName.value
			var major = document.Form.major.value
			var gpa = document.Form.gpa.value
			if ((id != "") && (lastName != "" || firstName != "" || major != "" || gpa != "")) {
				document.Form.page.type = "submit"
			}
			else {
				alert("Please fill out ID and at least one other field")
			}
		}
	</script>
  	</form>
  </body>
  </html>
UPDATE;
	if ($_POST["page"] == "Update") {
		$id = $_POST['id'];
		$lastName = $_POST['lastName'];
		$firstName = $_POST['firstName'];
		$major = $_POST['major'];
		$gpa = $_POST['gpa'];

  		$server = 'spring-2022.cs.utexas.edu';
  		$user = 'cs329e_bulko_jiaxin';
  		$pwd = 'knock8severe_longer';
  		$dbName = 'cs329e_bulko_jiaxin';


		$mysqli = new mysqli($server, $user, $pwd, $dbName);
		if ($mysqli->connect_errno) {
			die('Connect Error: ' . $mysqli->connect_errno . ': ' . $mysqli->connect_error);
		}
		else {
			//echo "<code>...Connecting successful</code><br>";
		}

		// Select Database
		$mysqli->select_db($dbName) or die($mysqli->error);
		
		if ($lastName != "") {
			if ($firstName != "") {
				if ($major != "") {
					if ($gpa != "") {
						$query = "UPDATE students SET lastName = '$lastName', firstName = '$firstName', major = '$major', gpa = '$gpa' WHERE id = '$id'";
					}
					else {
						$query = "UPDATE students SET lastName = '$lastName', firstName = '$firstName', major = '$major' WHERE id = '$id'";
					}
				}
				else {
					if ($gpa != "") {
						$query = "UPDATE students SET lastName = '$lastName', firstName = '$firstName', gpa = '$gpa' WHERE id = '$id'";
					}
					else {
						$query = "UPDATE students SET lastName = '$lastName', firstName = '$firstName' WHERE id = '$id'";
					}
				}
			}
			else {
				if ($major != "") {
					if ($gpa != "") {
						$query = "UPDATE students SET lastName = '$lastName', major = '$major', gpa = '$gpa' WHERE id = '$id'";
					}
					else {
						$query = "UPDATE students SET lastName = '$lastName', major = '$major' WHERE id = '$id'";
					}
				}
				else {
					if ($gpa != "") {
						$query = "UPDATE students SET lastName = '$lastName', gpa = '$gpa' WHERE id = '$id'";
					}
					else {
						$query = "UPDATE students SET lastName = '$lastName' WHERE id = '$id'";
					}
				}
			}
		}
		else {
			if ($firstName != "") {
				if ($major != "") {
					if ($gpa != "") {
						$query = "UPDATE students SET firstName = '$firstName', major = '$major', gpa = '$gpa' WHERE id = '$id'";
					}
					else {
						$query = "UPDATE students SET firstName = '$firstName', major = '$major' WHERE id = '$id'";
					}
				}
				else {
					if ($gpa != "") {
						$query = "UPDATE students SET firstName = '$firstName', gpa = '$gpa' WHERE id = '$id'";
					}
					else {
						$query = "UPDATE students SET firstName = '$firstName' WHERE id = '$id'";
					}
				}
			}
			else {
				if ($major != "") {
					if ($gpa != "") {
						$query = "UPDATE students SET major = '$major', gpa = '$gpa' WHERE id = '$id'";
					}
					else {
						$query = "UPDATE students SET major = '$major' WHERE id = '$id'";
					}
				}
				else {
					if ($gpa != "") {
						$query = "UPDATE students SET gpa = '$gpa' WHERE id = '$id'";
					}
				}
			}	
		}
							
		
		//$result = $mysqli->query($query) or die($mysqli->error);
		if ($mysqli->multi_query($query) === TRUE) {
			echo "<script>alert('SUCCESSFULLY UPDATED VALUES')</script>";
		}
		else {
			echo "<script>alert('FAIL TO UPDATE')</script>";
		}

		$mysqli->close();
	}

  }

 function DisplayDelete()
 {
  print <<<DELETE
  <html>
  <head>
  	<title> Action </title>
  	<link href="HW16.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "action" method = "post" action = "$script">
  	<h1> Delete Student Record </h1>
	<table>
		<tr>
			<td> ID: </td>
			<td> <input type = "number" name = "id" required> </td>
		</tr>
		<tr>
			<td> <button class = "actionBtn" onclick="window.location.href = 'HW16Action.php value = "Back to Actions" formnovalidate>Go Back</button></td>
			<td> <input name = "page" type = "submit" value = "Delete" class = "actionBtn"/> </td>
		</tr>
	</table>
  </form>
  </body>
  </html>
DELETE;
	if ($_POST["page"] == "Delete") {
		$id = $_POST['id'];

  		$server = 'spring-2022.cs.utexas.edu';
  		$user = 'cs329e_bulko_jiaxin';
  		$pwd = 'knock8severe_longer';
  		$dbName = 'cs329e_bulko_jiaxin';
		//echo $id . "<br>". $lastName."<br>".$firstName."<br>".$major."<br>".$gpa."<br>";


		$mysqli = new mysqli($server, $user, $pwd, $dbName);
		if ($mysqli->connect_errno) {
			die('Connect Error: ' . $mysqli->connect_errno . ': ' . $mysqli->connect_error);
		}
		else {
			//echo "<code>...Connecting successful</code><br>";
		}

		// Select Database
		$mysqli->select_db($dbName) or die($mysqli->error);
		//echo "<code>... Executing query</code><br>";
		$query = "DELETE FROM students WHERE id = '$id'";
		//$result = $mysqli->query($query) or die($mysqli->error);
		if ($mysqli->query($query) === TRUE) {
			echo "<script>alert('SUCCESSFULLY DELETED FROM DATABASE')</script>";
		}
		else {
			echo "<script>alert('FAIL TO DELETE')</script>";
		}
		$mysqli->close();
	}

  }

 function DisplayView()
 {
  $server = 'spring-2022.cs.utexas.edu';
  $user = 'cs329e_bulko_jiaxin';
  $pwd = 'knock8severe_longer';
  $dbName = 'cs329e_bulko_jiaxin';
  print <<<VIEW
  <html>
  <head>
  	<title> Action </title>
  	<link href="HW16.css" rel="stylesheet">
  </head>
  <body>
  	<form name = "Form" class = "action" method = "post" action = "$script">
  	<h1> View Student Record </h1>
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
			var lastName = document.getElementById("lastName").value
			var firstName = document.getElementById("firstName").value
			var id = document.getElementById("ID").value
			//var server = 'spring-2022.cs.utexas.edu'
			//var user = 'cs329e_bulko_jiaxin'
			//var pwd = 'knock8severe_longer'
			//var dbName = 'cs329e_bulko_jiaxin'
			var queryString = "?id=" + id + "&lastName=" + lastName + "&firstName=" + firstName + "&server=" + server + "&user=" + user + "&pwd=" + pwd + "&dbName=" + dbName
			ajaxRequest.open("GET", "HW16View.php" + queryString, true)
			ajaxRequest.send(null);
		}

		function Validate() {
			var id = document.Form.id.value
			var lastName = document.Form.lastName.value
			var firstName = document.Form.firstName.value
			if (id != "" || lastName != "" || firstName != "") {
				ajaxFunction('$server','$user','$pwd','$dbName')			
			}
			else {
				alert("Please fill out at least one field")
			}
		}

		function Check() {
			var id = document.Form.id.value
			var lastName = document.Form.lastName.value
			var firstName = document.Form.firstName.value
			if (id != "" || lastName != "" || firstName != "") {
				alert("Please Remove All Fields to View Entire Record")			
			}
			else {
				ajaxFunction('$server','$user','$pwd','$dbName')
			}
		}


	</script>

	<table>
		<tr>
			<td> ID: </td>
			<td> <input type = "number" name = "id" id = "ID"> </td>
		</tr>
		<tr>
			<td> Last Name: </td>
			<td> <input type = "text" name = "lastName" id = "lastName"> </td>
		</tr>
		<tr>
			<td> First Name: </td>
			<td> <input type = "text" name = "firstName" id = "firstName"> </td>
		</tr>
		<tr>
			<td colspan = "2"><input name = "showAll" type = "button" class = "actionBtn" onclick = "Check()" value = "View All Student Records"/></td>
		<tr>
			<td> <button class = "actionBtn" onclick="window.location.href = HW16Action.php" value = "Back to Actions" formnovalidate>Go Back</button></td>
			<td> <input name = "page" type = "button" onclick = "Validate()" value = "View" class = "actionBtn"/> </td>
		</tr>
	</table>
	<div id = "ajaxDiv"></div>
	</form>
  </body>
  </html>
VIEW;
  }

 function DisplayLogout()
 {
	echo "<script type='text/javascript'>";
	echo "alert('Logging Out. Thank You.');";
	echo "window.location.href = 'HW16.php';";
	echo "</script>";
 }

?>