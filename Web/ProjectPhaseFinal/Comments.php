<!DOCTYPE html>

<html lang="en">

<head>
    <title>About AET</title>
    <meta charset="UTF-8">
    <meta name="description" content="About AET Homepage">
    <meta name="author" content="Group1">
    <script src="CommentsJS.js"></script>
    <?php 
    $css = $_COOKIE["css"];
    if (!$css) { $css = "Homepage"; } 
    $sort = $_COOKIE["Sort"];
    if (!$sort) { $sort = "None"; setCookie("Sort", $sort, time() + 5184000); }
    ?>
    <link rel="stylesheet" href="<?php echo $css; ?>.css">
    <!-- <link rel="stylesheet" type="text/css" href="Homepage.css" />-->
    <link href="Images/logo.png" rel="icon">
</head> 

<body onload="ajaxFunction('spring-2022.cs.utexas.edu', 'cs329e_bulko_mka72', 'Fatal5Tune6pride', 'cs329e_bulko_mka72')">
    <div id="top">
        <a href = "Homepage.php" style="text-decoration: none">
            <img src="Images/logo.png" alt = "AET but it's in comic sans" width= "100" height="100" style= "float:left; position:relative; top:-20px">
            <h1>ABOUT AET</h1>
        </a>
        <a href="themeset.php?choice=Homepage&currentPage=Comments.php"><button class = "themeBtn">Normal</button></a>
        <a href="themeset.php?choice=HomepageDark&currentPage=Comments.php"><button class = "themeBtn">Dark</button></a>
    </div>

    <ul id="navlist">
        <li><a href="Homepage.php">Home</a></li>
        <li><a href="Courses.php">Courses</a></li>
        <li><a href="Faculty.php">Faculty</a></li>
        <li><a href="FAQ.php">FAQ</a></li>
        <li><a href="ContactUs.php">Contact Us</a></li>
        <li><a href="Comments.php">Comments</a></li>
	<li><a href="Login.php">Log In</a></li>
    </ul>
    <form method= "POST" id= "Comments" action = "Comments.php" onsubmit = "checkValid()">
	<script>
    		if ( window.history.replaceState ) {
        		window.history.replaceState( null, null, window.location.href );
   		 }
		function checkValid(){
            		if (courses.value == "--Select Course--"){
                		window.alert("Please select a course");
                		exit();
			}
            	}
		function ajaxFunction(server, user, pwd, dbName) {
			var ajaxRequest
			ajaxRequest = new XMLHttpRequest()
			ajaxRequest.onreadystatechange = function () {
				if (ajaxRequest.readyState == 4) {
					var ajaxDisplay = document.getElementById("ajaxDiv")
					ajaxDisplay.innerHTML = ajaxRequest.responseText
				}
			}
			var comment = document.getElementById("comments").value
			var rating = document.getElementById("ratings").value
			var courseName = document.getElementById("courses").value
			var queryString = "?rating=" + rating + "&courseName=" + courseName + "&comment=" + comment + "&server=" + server + "&user=" + user + "&pwd=" + pwd + "&dbName=" + dbName
			ajaxRequest.open("GET", "ViewRatings.php" + queryString, true)
			ajaxRequest.send(null);
		}
	</script>
        <div id="pagebody">
            <div id="subHeading">
                <h2>Comments</h2>
            </div> 
        </div>
        <div class = "commentspage">
          	<table id="RatingsFormTable">
			<?php 
				$userName = $_COOKIE['user']; 
				if ($userName == "") { 
					echo "<tr style='text-align: center'><th>Login to Comment</th><tr>";
				}
				else {
					echo "<tr style='text-align: center'><th>Hello $userName</th><tr>";
				}
			?>
			<tr>
				<th id="Courses" style="padding:20px; font-size:16pt"> Course:
					<select id = "courses" name = "courses">
						<option selected = "selected"> --Select Course-- </option>
						<option> Foundations of Art and Entertainment Technologies </option>
						<option> Foundations of Digital Imaging and Visualization </option>
						<option> Foundations of Creative Coding </option>
						<option> Foundations of Game Development </option>
						<option> Principles of Animation </option>
						<option> Concepts of Visual Style </option>
						<option> Game Character Animation </option>
						<option> 3D Modeling and Texturing </option>
						<option> AET Studio </option>
						<option> Gravitivity </option>
						<option> Tech Art </option>
						<option> Storyboard Concepts </option>
						<option> Video Game Prototyping </option>
						<option> Game Capstone </option>
					</select>
				</th>
			</tr>            
			<tr>
				<th id="Rating" style="padding:20px; font-size:16pt"> Rating:
					<select id = "ratings" name = "ratings">
						<option selected = "selected"> --No Rating-- </option>
						<option> Excellent </option>
						<option> Good </option>
						<option> Average </option>
						<option> Bad </option>
						<option> Extremely Poor </option>
					</select>
				</th>
			</tr>
			<tr>
				<th id = "Comments" style="padding:20px; font-size:16pt">
					<label for="comments">Comments:</label><br>
            				<textarea id="comments" name="comments" rows="6" cols="50">Enter Text</textarea>
				</th>
			</tr>
			<tr>
               	 		<th style="padding:20px"> 
					<input class = "themeBtn" name = "Insert" type = "submit" value = "Submit" style="position: relative; left: -5px">
                			<input class = "themeBtn" type = "reset" value = "Clear" style="position: relative; left: 10px"/> 
				</th>
			</tr>
		</table>
        </div> <!--commentspage-->
	</form>
	<div style="position:relative; left: -80%">
		<a href="Sort.php?currentPage=Comments.php&sort=None"><button class = "themeBtn">Time Sort</button></a>
		<a href="Sort.php?currentPage=Comments.php&sort=Name"><button class = "themeBtn">Name Sort</button></a>
    		<a href="Sort.php?currentPage=Comments.php&sort=Rating"><button class = "themeBtn">Rate Sort</button></a>
	</div>
<?php
	session_start();
	//$userName = $_COOKIE["user"];
       	//echo "this is my username: " .$userName;
	if ($_POST["Insert"] == "Submit" && $_POST["courses"] != "--Select Course--") {
		if ($userName != "") {
			$courseName = $_POST["courses"];
			$rating = $_POST["ratings"];
			$comments = $_POST["comments"];

			$server = 'spring-2022.cs.utexas.edu';
  			$user = 'cs329e_bulko_mka72';
  			$pwd = 'Fatal5Tune6pride';
  			$dbName = 'cs329e_bulko_mka72';

			$mysqli = new mysqli($server, $user, $pwd, $dbName);
			if ($mysqli->connect_errno) {
				die('Connect Error: ' . $mysqli->connect_errno . ': ' . $mysqli->connect_error);
			}
			else {
				//echo "<code>...Connecting successful</code><br>";
			}
			$mysqli->select_db($dbName) or die($mysqli->error);
			$query = "INSERT INTO ratings VALUES ('$rating', '$courseName', '$comments')";
			//$result = $mysqli->query($query) or die($mysqli->error);
			if ($mysqli->query($query) === TRUE) {
				//echo "SUCCESSFULLY INSERTED INTO DATABASE";
			}
			else {
				echo "FAIL TO INSERT";
			}
			$mysqli->close();
		}
		else {
			echo '<script type="text/javascript">alert("Please Login to Comment"); document.location="Login.php";</script>';	
		}
	}
?>
    <div id = "ajaxDiv"></div>
    <div id = "footer">
        Melina Rosales, Jiaxin Huang, Soo Aguilar, Micah Chow
        <span style = "margin-left: 30px" > Updated on May 6, 2022 </span>
    </div> <!--footer -->
</body>
</html>