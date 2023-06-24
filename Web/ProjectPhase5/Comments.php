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
    ?>
    <link rel="stylesheet" href="<?php echo $css; ?>.css">
    <!-- <link rel="stylesheet" type="text/css" href="Homepage.css" />-->
    <link href="Images/logo.png" rel="icon">
</head> 

<body>
    <div id="top">
        <a href = "Homepage.php" style="text-decoration: none">
            <img src="Images/logo.png" alt = "AET but it's in comic sans" width= "100" height="100" style= "float:left; position:relative; top:-20px">
            <h1>ABOUT AET</h1>
        </a>
        <a href="themeset.php?choice=Homepage&currentPage=Comments.php"><button id = "themeBtn">Normal</button></a>
        <a href="themeset.php?choice=HomepageDark&currentPage=Comments.php"><button id = "themeBtn">Dark</button></a>
    </div>

    <ul id="navlist">
        <li><a href="Homepage.php">Home</a></li>
        <li><a href="Courses.php">Courses</a></li>
        <li><a href="Faculty.php">Faculty</a></li>
        <li><a href="FAQ.php">FAQ</a></li>
        <li><a href="ContactUs.php">About Us</a></li>
        <li><a href="Comments.php">Contact Us</a></li>
    </ul>
    <form method= "POST" id= "Comments" onsubmit="validate()" action = "thankyou.php">
        <div id="pagebody">
            <div id="subHeading">
                <h2>Contact Us</h2>
            </div> 
        </div>
        <div class = "commentspage">
            <p>
                <label> Name: <input name = "name" type = "text" size = "30" required /> </label>
            </p>
            <p>
                <label> Email: <input name = "email" type = "password" size = "30" required /> </label>
            </p>
            <p>
                I am a: <br>
                <label> <input name = "connection" type = "radio" value = "current" /> Current AET Student </label><br>
                <label> <input name = "connection" type = "radio" value = "prospective" /> Prospective AET Student</label><br>
                <label> <input name = "connection" type = "radio" value = "family/friend" /> Family/Friend of AET Student/Prospective AET Student</label><br>
                <label> <input name = "connection" type = "radio" value = "other" checked /> Other</label><br>
            </p>
            <label for="comments">Questions/Comments:</label><br>
            <textarea id="comments" name="comments" rows="6" cols="50">Enter Text</textarea>
            <br>
            <p>
                <input name = "submitform" type = "submit" value = "Submit">
                <input type = "reset" value = "Clear" />
            </p>
            <br>
        </div> <!--commentspage-->
    </form>
    <div id = "footer">
        © Melina Rosales, Jiaxin Huang, Soo Aguilar, Micah Chow
        <span style = "margin-left: 30px" > Updated on April 18, 2022 </span>
    </div> <!--footer -->
</body>
</html>