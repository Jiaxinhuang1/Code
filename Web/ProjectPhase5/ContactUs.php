<!DOCTYPE html>

<html lang="en">

<head>
    <title>Website About Us Page</title>
    <meta charset="UTF-8">
    <meta name="description" content="layout for AET homepage">
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
        <a href="themeset.php?choice=Homepage&currentPage=ContactUs.php"><button id = "themeBtn">Normal</button></a>
        <a href="themeset.php?choice=HomepageDark&currentPage=ContactUs.php"><button id = "themeBtn">Dark</button></a>
    </div>

    <ul id="navlist">
        <li><a href="Homepage.php">Home</a></li>
        <li><a href="Courses.php">Courses</a></li>
        <li><a href="Faculty.php">Faculty</a></li>
        <li><a href="FAQ.php">FAQ</a></li>
        <li><a href="ContactUs.php">About Us</a></li>
        <li><a href="Comments.php">Contact Us</a></li>
    </ul>
    
    <div id="pagebody">
        <div id="subHeading">
            <h2>About Us</h2>
        </div> <!--subHeading-->
        <div id="content">
            <figure class="about">
                <h3> Jiaxin Huang</h3>
                <img src="Images/jiaxin.png" alt="Picture of jiaxin"> 
                <figcaption> 
                    <b>Emphasis: </b> Game Development (Programming/Scripting) <br>
                    <b>Hobbies: </b> Sleep, Read novels, Watch drama/anime <br>
                    <b>Favorite Food: </b> Dumplings and Boba <br>
                    <b>Favorite Game: </b> Latale <br>
                    <a href="https://jhuangrgchs.wixsite.com/website">Look at my Portfolio</a>
                </figcaption>
            </figure>
            <figure class="about">
                <h3> Soo Jung Aguilar</h3>
                <img src="Images/soo.png" alt="Picture of soo"> 
                <figcaption>
                    <b>Emphasis: </b> Game Development / Digital Visualization <br>
                    <b>Hobbies: </b> Sketching, Admiring my cat <br>
                    <b>Favorite Food: </b> Sushi <br>
                    <b>Favorite Game: </b> Genshin / Splatoon <br>
                    <a href="https://www.artstation.com/sooaguilar">Look at my Portfolio</a>
                </figcaption>
            </figure>
            <figure class="about">
                <h3> Melina Rosales</h3>
                <img src="Images/melina.png" alt="Picture of melina"> 
                <figcaption> 
                    <b>Emphasis: </b> Game Development / Digital Visualization <br>
                    <b>Hobbies: </b> Drawing, Gardening <br>
                    <b>Favorite Food: </b> Peaches <br>
                    <b>Favorite Game: </b> Monster Hunter <br>
                    <a href="https://www.artstation.com/melinarosales">Look at my Portfolio</a>
                </figcaption>
            </figure>
            <figure class="about">
                <h3> Micah Chow</h3>
                <img src="Images/micah.png" alt="Picture of micah"> 
                <figcaption> 
                    <b>Emphasis: </b> Game Development / Digital Visualization <br>
                    <b>Hobbies: </b> Drawing, Reading Comics <br>
                    <b>Favorite Food: </b> Candy <br>
                    <b>Favorite Game: </b> Stardew Valley <br>
                    <a href="https://www.artstation.com/andredsen">Look at my Portfolio</a>
                </figcaption>
            </figure>
        </div>
    </div> <!-- pagebody -->
    <div id = "footer">
            © Melina Rosales, Jiaxin Huang, Soo Aguilar, Micah Chow
            <span style = "margin-left: 30px" > Updated on April 18, 2022 </span>
    </div> <!--footer -->
</body>

</html>
