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
            <img src="Images/logo.png" alt = "AET but it's in comic sans" width= "100" height="100" style= "float:left; position:relative; top:-20px;">
            <h1>ABOUT AET</h1>
        </a>
        <a href="themeset.php?choice=Homepage&currentPage=Courses.php"><button id = "themeBtn">Normal</button></a>
        <a href="themeset.php?choice=HomepageDark&currentPage=Courses.php"><button id = "themeBtn">Dark</button></a>
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
                <h2>Courses</h2>

            </div> 
        </div>

        <!--I'm going to kermit.. Drop some???-->
        <div id = "Showcase">
                <img id="bigPicWork" alt="example student work" width = "350" height="350" src="ExampleWork/foundations2.gif" class = hasArray>
                <div class="caption">Student Work Showcase</div>
        </div>

        <div id = "Tables">
            <table> 
                <caption><strong>Lower Division Courses</strong></caption>
                <tr>
                    <td class = "name"><b>Foundations of Art/Entertainment Tech</b><br><br>
                        Introduction to the core concepts of the three emphases of the Center for Arts and Entertainment Technologies: Music and Sound, New Performance Technologies, and Game and Mobile Media Applications.</td>
                    <td><img id="foundationsImage" alt="example student work" width = "250" height="250" src="ExampleWork/foundations1.png" class = hasArray></td>
                </tr>
                <tr>
                    <td class = "name"><b>Foundations of Digital Imaging and Visualization</b><br><br>
                        An introduction to digital graphic art software and practices including aesthetics, design, production, and publishing.</td>
                    <td><img id="306Image" alt="example student work" width = "250" height="250" src="ExampleWork/3060.PNG" class = hasArray></td>
                </tr>
                <tr>
                    <td class = "name"><b>Foundations of Creative Coding</b><br><br>
                        A guide for expressing original ideas directly in computer code using the graphics language Processing.</td>
                    <td><img id="CreativeCodingImage" alt="example student work" width = "250" height="250" src="ExampleWork/creatingCoding2.PNG" class = hasArray></td>
                </tr>
                <tr>
                    <td class = "name"><b>Foundations of Game Development</b><br><br>
                        An introduction to the process of creating games from concept through publishing including aesthetics, design and production.</td>
                    <td><img id="gameDesignImage" alt="example student work" width = "250" height="250" src="ExampleWork/gamedesign1.png"></td>
                </tr>

            </table>
            <br>

            <table> 
                <caption><strong>Upper Division Courses</strong></caption>

                <tr>
                    <td class = "name"><b>Principles of Animation</b><br><br>
                        An introduction to the principles of animation for 2D and 3D graphics.</td>
                    <td><img id="pOfAnimationImage" alt="example student work" width = "250" height="250" src="Images/walk.gif"></td>
                </tr>

                <!-- <tr>
                    <td class = "name"><b>Interactive Music</b><br>
                        Create real-time interactive music using Ableton Live and Musical Instrument Digital Interface (MIDI) controllers.</td>
                    <td><button onclick="">Play Student Example</button>  <button onclick="">Stop</button></td>
                </tr> -->

                <tr>
                    <td class = "name"><b>Concepts of Visual Style </b><br><br>
                        Explore the fundamentals of artistic style and apply them to the techniques of concept art. </td>
                    <td><img id="conceptsOVSImage" alt="example student work" width = "250" height="250" src="ExampleWork/ConceptsOVS1.png" class = hasArray></td>
                </tr>

                <tr>
                    <td class = "name"><b>Game Character Animation</b><br><br>
                        Learn the process of creating 3D gameplay animations, techniques to improve animation workflow, and how to implement animations into Unreal Engine. </td>
                    <td><img id="gameCharaAniImage" alt="example student work" width = "250" height="250" src="ExampleWork/mandT1.png"></td>
                </tr>

                <tr>
                    <td class = "name"><b>3D Modeling and Texturing</b><br><br>
                        An introduction to 3D modeling and texturing techniques used in game development and visualization.</td>
                    <td><img id="3DMandTImage" alt="example student work" width = "250" height="250" src="ExampleWork/mandT2.png"></td>
                </tr>

                <tr>
                    <td class = "name"><b>AET Studio</b><br><br>
                        Experiment and design projects with faculty guidance.</td>
                    <td><img id="aetStudioImage" alt="example student work" width = "250" height="250" src="ExampleWork/aetstudio1.png" class = hasArray></td>
                </tr>

                <tr>
                    <td class = "name"><b>Gravitivity</b><br><br>
                        Create and explore artistic concepts within the theme of "weightlessness".</td>
                    <td><img id="gravitivityImage" alt="example student work" width = "250" height="250" src="ExampleWork/gravitivity.png"></td>
                </tr>

                <!-- <tr>
                    <td><b>Audio Processing</b><br>
                        Explores the use of sound-shaping tools, convolution reverb, noise reduction, pitch and time editing to make precise corrections to audio files.</td>
                    <td><button onclick="">Play Student Example</button> <button onclick="">Stop</button></td>
                </tr> -->

                <tr>
                    <td class = "name"><b>Tech Art</b><br><br>
                        Examine the technical aspects of game content creation including: shaders, automation, tool creation, and special effects. Partially taught as a Web-based course.</td>
                    <td><img id="techArtImage" alt="example student work" width = "250" height="250" src="ExampleWork/techart1.png" class = hasArray></td>
                </tr>

                <tr>
                    <td class = "name"><b>Storyboard Concepts</b><br><br>
                        Learn storyboard terminology, concepts, and techniques for effective visual communication and storytelling. </td>
                    <td><img id="storyboardImage" alt="example student work" width = "250" height="250" src="ExampleWork/storyBoard1.PNG"></td>
                </tr>

                <tr>
                    <td class = "name"><b>Video Game Prototyping</b><br><br>
                        Explore rapid prototyping techniques for video game art and design usingideation, storyboarding, pitching, prototyping, testing, and documentation.</td>
                    <td><img id="protypingImage" alt="example student work" width = "250" height="250" src="ExampleWork/videogameprototyping1.png"></td>
                </tr>
                <tr>
                    <td class = "name"><b>Game Capstone</b><br><br>
                        Work in small teams from different disciplines to develop 3D or 2D games.</td>
                    <td><img id="gameCapstoneImage" alt="example student work" width = "250" height="250" src="ExampleWork/gamecapstone1.png" class = hasArray></td>
                </tr>

            </table>
        </div>

        <div id = "footer">
            © Melina Rosales, Jiaxin Huang, Soo Aguilar, Micah Chow
            <span style = "margin-left: 30px" > Updated on April 18, 2022 </span>
        </div> <!--footer -->

        <script>
            function startSlideShow(workArray, idString){
                currentIndex = -1
                intervalID = setInterval(function(){
                    $("#bigPicWork").fadeOut(10,function() {})

                    currentIndex = (currentIndex + 1) % workArray.length
                    document.getElementById(idString).src = workArray[currentIndex] 
                    $("#bigPicWork").fadeIn(500, function() {})

                },10000 )  
            }

            function onLoad(){
                var workArray = new Array("ExampleWork/foundations2.gif", "ExampleWork/mandT1.png", "ExampleWork/foundations3.gif", "ExampleWork/creatingCoding1.PNG", "ExampleWork/ConceptsOVS2.png", "ExampleWork/aetstudio2.png", "ExampleWork/3062.PNG", "ExampleWork/3063.PNG", "ExampleWork/GAP1.png", "ExampleWork/mobileGame2.png", "ExampleWork/techart2.png", "ExampleWork/MandT2.png", "ExampleWork/storyBoard2.PNG")

                startSlideShow(workArray, "bigPicWork")

            }
        </script>
    </body>
</html>