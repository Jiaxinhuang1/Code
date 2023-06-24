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
        <a href="themeset.php?choice=Homepage&currentPage=Faculty.php"><button id = "themeBtn">Normal</button></a>
        <a href="themeset.php?choice=HomepageDark&currentPage=Faculty.php"><button id = "themeBtn">Dark</button></a>
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
            <h2>Faculty</h2>
        </div> <!--subHeading-->
        <div id = "facultyRow">
            <h3 style = "margin-bottom: -25px;"> LEADERSHIP </h3>
            <p> Assistant Dean of SDCT: <a href="https://designcreativetech.utexas.edu/doreen-lorenzo">Doreen Lorenzo</a> </p>
            <p> Chair of Department of AET: <a href="https://designcreativetech.utexas.edu/michael-baker">Michael Baker</a> </p>
            <h3 style = "margin-top: 50px; margin-bottom: -25px;"> STAFF </h3>
            <p> Academic Advisor: <a href="https://designcreativetech.utexas.edu/doris-gilber">Doris Gilbert</a> </p>
            <p> Industry Relations Manager: <a href="https://designcreativetech.utexas.edu/jamil-hooper">Jamil Hooper</a> </p>
            <p> Communications and Industry Relations Assistant: <a href="https://designcreativetech.utexas.edu/michaela-newman">Michaela Newman</a> </p>
            <p> Undergraduate Admissions Coordinator: <a href="https://designcreativetech.utexas.edu/david-rezaei">David Rezaei</a> </p>
            <h3 style = "margin-top: 50px; margin-bottom: -25px;"> Faculty/Professors </h3>
            <p> <a href="https://designcreativetech.utexas.edu/taylor-bancroft">Taylor Bancroft</a> </p>
                <ul>
                    <li> Full Stack Engineer, Developer </li>
                    <li> Courses Taught (2021-2022): AET 319 (Media and Technology) </li>
                </ul>   
            <p> <a href="https://designcreativetech.utexas.edu/bill-byrne">Bill Byrne</a> </p>
                <ul>
                    <li> Multimedia Digital Artist, Game Artist, Motion Graphics Designer </li>
                    <li> Courses Taught (2021-2022): AET 319 (Art and Content), AET 334E (Video Game Art Pipeline), AET 327C (Advanced Motion Graphics), AET 339 (Portfolio Development), AET 339 (Audio Reactive Visuals) 
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/deepak-chetty-mfa">Deepak Chetty</a> </p>
                <ul>
                    <li> Director, Cinematographer, VFX/XR Desginer </li>
                    <li> Courses Taught (2021-2022): AET 339 (Concepts of Real Time Rendering), AET 339 (Virtual Production) 
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/kyle-chittenden-ma">Kyle Chittenden</a> </p>
                <ul>
                    <li> Game Animator, Tech Animator </li>
                    <li> Courses Taught (2021-2022): AET 333 (Game Character Animation, Previously known as Realtime Animation Techniques) 
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/david-cohen">David Cohen</a> </p>
                <ul>
                    <li> Game Producer, Game Designer </li>
                    <li> Courses Taught (2021-2022): AET 319 (Design and Interactivity), AET 318C (Foundations of Video Game Development), AET 336C (Video Game History and Culture), AET 339 (Narrative Design), AET 372 (Senior Design Projects I), AET 373 (Senior Design Projects II)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/tyler-coleman">Tyler Coleman</a> </p>
                <ul>
                    <li> Independent Game Developer, Game Programmer </li>
                    <li> Courses Taught (2021-2022): AET 310 (Foundations of Creative Coding), AET 333 (Procedural Generation in Games), AET 334F (Video Game Scripting), AET 334M (Video Game Systems Design), AET 339 (Physical Game Design), AET 339 (Mobile Game Design)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/jessie-contour-mfa">Jessie Contour</a> </p>
                <ul>
                    <li> Designer, Technical Animator </li>
                    <li> Courses Taught (2021-2022): AET 319 (Media and Technology), AET 330 (Tech Art 1), AET 339 (Future of Gaming with Dell), AET 339 (Next Level Cosplay), AET 339 (Next Level Arcade)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/neal-daugherty">Neal Daugherty</a> </p>
                <ul>
                    <li> Digital Artist, Designer </li>
                    <li> Courses Taught (2021-2022): AET 306 (Foundations of Digital Imaging and Visualization), AET 319 (Art and Content), AET 324E (Concepts of Visual Style), AET 339 (Motion and Animation, Previously known as Introduction to 2D Animation), AET 339 (Design Studio: “Gravitivity”)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/natasha-davison">Natasha Davison</a> </p>
                <ul>
                    <li> Television Producer, Writer, Director </li>
                    <li> Courses Taught (2021-2022): AET 339 (Business of Entertainment)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/lucas-dimick">Lucas Dimick</a> </p>
                <ul>
                    <li> Artist, Independent Animator </li>
                    <li> Courses Taught (2021-2022): AET 324D (Principles of Animation), AET 339 (Storyboard Concepts)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/kyle-evans">Kyle Evans</a> </p>
                <ul>
                    <li> Sound Designer, New Media Artist </li>
                    <li> Courses Taught (2021-2022): AET 305 (Foundations of Music Technology), AET 310 (Foundations of Creative Coding), AET 319 (Sound and Space), AET 339 (Immersive Pop-ups), AET 339 (DIY Synthesizers)
                    </li>
                </ul>
                <p> <a href="https://designcreativetech.utexas.edu/eric-freeman">Eric Freeman</a> </p>
                <ul>
                    <li> Computer Science Ph.D., Author </li>
                    <li> Courses Taught (2021-2022): AET 310 (Foundations of Creative Coding)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/mk-haley">MK Haley</a> </p>
                <ul>
                    <li> Themed Entertainment Designer, Producer </li>
                    <li> Courses Taught (2021-2022): AET 330T (Digital Design Experience), AET 339 (Themed Entertainment Design), AET 339 (Nimble Design for Tough Times), AET 339 (Storytelling with Mini Golf)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/jose-kozan">Jose Kozan</a> </p>
                <ul>
                    <li> AR/MR/XR Designer, Architect </li>
                    <li> Courses Taught (2021-2022): AET 330T (Mixed Reality for the Masses), AET 339 (Storytelling with AR)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/yuliya-lanina">Yuliya Lanina</a> </p>
                <ul>
                    <li> Multimedia Artist, Performer </li>
                    <li> Courses Taught (2021-2022): AET 339 (Drawing for Designers), AET 339 (Gensler DXD Studio Partnership), AET 339 (Humor in Storytelling), AET 372 (Senior Design Projects I), AET 373 (Senior Design Projects II)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/sam-lipman-mm">Sam Lipman</a> </p>
                <ul>
                    <li> Multimedia Composer </li>
                    <li> Courses Taught (2021-2022): AET 323E (Video Game Audio I), AET 341C (Virtual Instruments), AET 341D (Digital Musicianship), AET 321C (Audio Processing)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/chris-meunchow">Chris Muenchow</a> </p>
                <ul>
                    <li> Technical Product Manager </li>
                    <li> Courses Taught (2021-2022): AET 348 (Concert and Event Lighting)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/shannon-murray">Shannon Murray</a> </p>
                <ul>
                    <li> Writer, Storyteller </li>
                    <li> Courses Taught (2021-2022): AET 339 (Intro to Narrative)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/sven-ortel">Sven Ortel</a> </p>
                <ul>
                    <li> Projection Designer </li>
                    <li> Courses Taught (2021-2022): AET 344F (Design Skills: Projection), AET 348G: Media Design and Technology)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/isaac-oster">Isaac Oster</a> </p>
                <ul>
                    <li> Technical Artist, 3D Game Artist </li>
                    <li> Courses Taught (2021-2022): AET 319 (3D Foundations), AET 326C (3D Modeling and Texturing)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/chris-ozley-dma">Chris Ozley</a> </p>
                <ul>
                    <li> Music Composer and Arranger </li>
                    <li> Courses Taught (2021-2022): AET 320G (Audio Coding I), AET 323D (Interactive Music), AET 339 (Generative Audio Programming), AET 350 (Computer Music Project)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/chip-sbrogna">Chip Sbrogna</a> </p>
                <ul>
                    <li> Game and Level Designer </li>
                    <li> Courses Taught (2021-2022): AET 333 (Challenges in Game Design)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/matt-smith">Matt Smith</a> </p>
                <ul>
                    <li> Projection Designer </li>
                    <li> Courses Taught (2021-2022): AET 316C (Foundations of PLAI), AET 319 (Sound and Space), AET 329F (Projection Mapping), AET 339 (SR Design Project Story Mode), 344D (3D Previsualization for Live Entertainment), AET 348C (Live Event Engineering)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/honoria-starbuck-phd">Honoria Starbuck</a> </p>
                <ul>
                    <li> International Artist </li>
                    <li> Courses Taught (2021-2022): Courses Taught (2021-2022): AET 304 (Foundations of AET), AET 319 (Design and Interactivity)
                    </li>
                </ul>
            <p> <a href="https://designcreativetech.utexas.edu/paul-toprac">Paul Toprac</a> </p>
                <ul>
                    <li> UT GDAD Program Associate Director, Game and Software Developer </li>
                    <li> Courses Taught (2021-2022): AET 376 (Game Development Capstone: 2D Games), AET 377 (Game Development Capstone: 3D Games)
                    </li>
                </ul>
        </div> <!-- facultyRow -->
        <div id = "facultyImgRow" >
            <img src="Images/faculty1.jpeg" alt="Picture of Doreen Lorenzo with Students">
            <p style = "font-size: 12px; margin-top: 2px; margin-bottom: 15px;"> Image Credits: UT News </p>
            <img src="Images/faculty2.jpeg" alt="Picture of AET Students">
            <p style = "font-size: 12px; margin-top: 2px; margin-bottom: 15px;"> Image Credits: Austin Inno </p>
            <img src="Images/faculty3.jpeg" alt="Picture of MK Haley with Students">
            <p style = "font-size: 12px; margin-top: 2px; margin-bottom: 15px;"> Image Credits: UT SDCT Website </p>
            <img src="Images/faculty4.jpeg" alt="Picture of Matthew Smith with Student">
            <p style = "font-size: 12px; margin-top: 2px; margin-bottom: 15px;"> Image Credits: UT SDCT Website </p>
            <img src="Images/faculty5.jpeg" alt="Picture of Chris Ozley with Student">
            <p style = "font-size: 12px; margin-top: 2px; margin-bottom: 15px;"> Image Credits: UT SDCT Website </p>
        </div> <!-- facultyImgRow -->
    </div> <!-- pagebody -->
    <div id = "footer">
            © Melina Rosales, Jiaxin Huang, Soo Aguilar, Micah Chow
            <span style = "margin-left: 30px" > Updated on April 18, 2022 </span>
    </div> <!--footer -->
    
</body>
</html>