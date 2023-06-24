<!DOCTYPE html>

<html lang="en">

<head>
    <title>About AET</title>
    <meta charset="UTF-8">
    <meta name="description" content="About AET Homepage">
    <meta name="author" content="Group1">
    <?php
        $css = $_COOKIE["css"];
        if (!$css) { $css = "Homepage"; }
    ?>
    <link rel="stylesheet" href="<?php echo $css; ?>.css">
    <!-- <link rel="stylesheet" type="text/css" href="Homepage.css" />-->
    <link href="Images/logo.png" rel="icon">
    <script type = "text/javascript" src = "FormValidation.js"></script></head>
<body>

    <div id="top">
        <a href = "Homepage.php" style="text-decoration: none">
            <img src="Images/logo.png" alt = "AET but it's in comic sans" width= "100" height="100" style= "float:left; position:relative; top:-20px">
            <h1>ABOUT AET</h1>
        </a>
        <a href="themeset.php?choice=Homepage&currentPage=Login.php"><button class = "themeBtn">Normal</button></a>
        <a href="themeset.php?choice=HomepageDark&currentPage=Login.php"><button class = "themeBtn">Dark</button></a>
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

    <div id = "pagebody">
    <div id="subHeading">
            <h2>Log in</h2>
        </div> <!--subHeading-->
    </div>
<?php
	if (session_status() === PHP_SESSION_NONE) {
   	 	session_start();
	}	
	if (!isset($_SESSION["user"]) || $_SESSION["user"] == "")
	{
		if ($_POST["page"] == "Register") {
                	registerPage();
        	} else {
            		loginPage();
   	 	}
    		//$_SESSION["user"] = "";
	}
	else {
		DisplayGreeting();
	}
	if ($_POST["page"] == "Logout") {
		session_unset();
		session_destroy();
		setCookie("user", $user, time()-3600);
		header("Location: Login.php");
	}

    function DisplayGreeting()
    {
            $script = $_SERVER['PHP_SELF'];
	    $userName = $_SESSION["user"];
	    echo "<form method = 'POST' action = '$script'>";
            echo "<table id = 'LoginTable' style='margin-top:50px; margin-bottom:150px'><tr><th>";
            echo "Hello, Welcome to About AET! <br> $userName";
	    echo "</th></tr>";
	    echo "<tr><th><input type = 'submit' name = 'page' value = 'Logout' class = 'loginBtn'/></th></tr>";
	    echo "</table>";
	    echo "</form>";
		
    }


    function loginPage()
    {
            $script = $_SERVER['PHP_SELF'];
            print <<<LOGIN
<form method = "POST" action = "checkLogin.php">
        <table id = "LoginTable" style="margin-top:50px; margin-bottom:150px">
        <tr>
            <td style="padding-bottom:10px">Username:</td>
                <td style="padding-bottom:10px"> <input name = "user" id = "user" type = "text" size = "30" required/> </td>
        </tr>
        <tr>
                <td style="padding-bottom:10px">Password:</td>
                <td style="padding-bottom:10px"> <input name = "pwd" id = "pwd" type = "password" size = "30" required /> </td>
        </tr>
	<tr>
		<td style="padding-bottom:10px"><input name = "login" type = "submit" value = "Login" class = "loginBtn"/></form></td>
	</tr>
	<tr>
		<td style="padding-bottom:10px" colspan = "2"><form method = "POST" action = "$script">
        		Don't have an account? <input name = "page" type = "submit" value = "Register" class = "loginBtn"/>
        	</form></td>
	</tr>
        </table>
LOGIN;
        }

    function registerPage()
    {
            $script = $_SERVER['PHP_SELF'];
            print <<<REGISTER
<form method = "POST" action = "checkLogin.php" name="RegistrationForm" id = "LoginForm">
        <table id = "LoginTable" style="margin-top:50px; margin-bottom:150px">
        <tr>
            <td style="padding-bottom:10px">Username:</td>
                <td style="padding-bottom:10px"> <input name = "user" type = "text" size = "30" required/> </td>
        </tr>
        <tr>
                <td style="padding-bottom:10px">Password:</td>
                <td style="padding-bottom:10px"> <input name = "pwd" type = "password" size = "30" required /> </td>
        </tr>
        <tr>
            <td style="padding-bottom:10px">Confirm Password:</td>
            <td style="padding-bottom:10px"> <input name = "confirmpwd" id = "confirmpwd" type = "password" size = "30" required /></td>
    	</tr>
	<tr>
		<td style="padding-bottom:10px">
        		<input id = "RegisterBtn" name = "register" type = "button" onclick="Validate()" value = "Join" class = "loginBtn"/></form></td>
		<td style="padding-bottom:10px"><form method = "POST" action = "$script"><input name = "page" type = "submit" value = "Back" class = "loginBtn"/></form></td>
	</tr>
    </table>
REGISTER;
        }

?>
    <div id = "footer">
        Melina Rosales, Jiaxin Huang, Soo Aguilar, Micah Chow
        <span style = "margin-left: 30px" > Updated on May 6, 2022 </span>
    </div> <!--footer -->
</body>
</html>