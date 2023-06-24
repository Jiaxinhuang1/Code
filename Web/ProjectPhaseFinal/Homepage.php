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
</head> 

<body>

    <div id="top">
        <a href = "Homepage.php" style="text-decoration: none">
            <img src="Images/logo.png" alt = "AET but it's in comic sans" width= "100" height="100" style= "float:left; position:relative; top:-20px">
            <h1>ABOUT AET</h1>
        </a>
        <a href="themeset.php?choice=Homepage&currentPage=Homepage.php"><button class = "themeBtn">Normal</button></a>
        <a href="themeset.php?choice=HomepageDark&currentPage=Homepage.php"><button class = "themeBtn">Dark</button></a>
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
    
    <div id="pagebody">
        <div id="subHeading">
            <h2>Welcome Prospective AET Students!</h2>
        </div> <!--subHeading-->
        <div id="leftPara">
            <p>
                This is a site for AET students by AET students. AET stands for the B.S in Art and Entertainment Technology at UT Austin. AET focuses on game design, visualization, and sound design. You can find courses on game development, 3D modeling, and more. Here you can get to know the program, the classes, the professors and prospective careers. You can also look at work from former students. If you have any questions, feel free to visit the FAQ or contact us. <br> <b>Hook Em :D</b>
            </p>
        </div> <!--leftPara-->
        <div id="PhotoCollection">
            <br>
            <img src="Images/homepageImage2.png" width="200" height="200" style="float:right" position = "relative">
            <img src="Images/sound.png" width="200" height="200" style="float:right" position = "relative">
        </div> <!--PhotoCollection-->
        <div id="PhotoCollection2">
            <img src="Images/plai.png" width="250" height="200" style="float:right" position = "relative">
            <br>
            <img src="Images/game.png" width="250" height="200" style="float:right" position = "relative">
            <br>
		<div style = "width: 100%; position:relative; left: -130%; top: 10px">
                	<iframe style = "" allowfullscreen="" frameborder="0" height="540" src="https://player.vimeo.com/video/460708506" width="960"></iframe>
        	</div>
	</div> <!--PhotoCollection2-->
    </div> <!-- pagebody -->
    
    <div id = "footer">
        Melina Rosales, Jiaxin Huang, Soo Aguilar, Micah Chow
        <span style = "margin-left: 30px" > Updated on May 6, 2022 </span>
    </div> <!--footer --> 
</body>
</html>