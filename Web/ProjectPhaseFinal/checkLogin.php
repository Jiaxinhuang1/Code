<?php

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

$mysqli->select_db($dbName) or die($mysqli->error);

// if(! $connect ) {
//     die('Could not connect: ' . mysql_error());
// }

// MAKE SESSION

session_start();
$user = "";
if (!isset($_SESSION["user"]))
{
    $_SESSION["user"] = "";
}

if(isset($_POST['login'])){
    $user = $_POST['user'];
    $pass = $_POST['pwd'];

    // Escape User Input to help prevent SQL Injection
    $user = $mysqli->real_escape_string($user);
    $pass = $mysqli->real_escape_string($pass);
    //Build query
    $query = "SELECT username, password FROM login_info WHERE username= '$user' AND password= '$pass' ";
    //Execute query
    $result = $mysqli->query($query) or die($mysqli->error);
    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
    $count = mysqli_num_rows($result);

    if($count == 1){
        $_SESSION['user'] = $user;
	setCookie("user", $user, 0);
        header("location: Homepage.php");
    }  
    else{
        echo '<script type="text/javascript">alert("Please enter a valid login"); document.location="Login.php";</script>'; exit();
    }
    $mysqli->close();

}

if(isset($_POST['register'])){
    $user = $_POST['user'];
    $pwd = $_POST['pwd'];
    $pwd    = urldecode($pwd);
    $confirmedPass = $_POST['confirmpwd'];
    //if($pwd != $confirmedPass) {
    //    echo '<script type="text/javascript">alert("Password Must Match"); document.location="Login.php"</script>';
    //} else {
    $query = "INSERT INTO login_info VALUES ('$user', '$pwd')";
    //$result = $mysqli->query($query) or die($mysqli->error);
    if ($mysqli->query($query) === TRUE) {
    	$_SESSION['user'] = $user;
	setCookie("user", $user, 0);
        header("location: Homepage.php");
    }
    else {
        echo '<script type="text/javascript">alert("Username used"); document.location="Login.php"</script>';
    }
    $mysqli->close();
}

?>