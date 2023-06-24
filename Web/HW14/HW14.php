<!DOCTYPE html>

<html lang="en">

<head>
   <title>HW14</title>
   <meta charset="UTF-8">
   <meta name="description" content="Newspaper Login Using Cookies">
   <meta name="author" content="Jiaxin Huang">
   <link href="HW14.css" rel="stylesheet">
   <script type = "text/javascript"> </script>
</head>

<body>
   <div id="container">
      <div id="top">
         <h1>The Daily Anime Newspaper</h1>
         <h3>Austin, TX - Saturaday April 17, 2022</h3>
      </div>
      <div class="headlines">
         <?php
	    setcookie("page", "HW14NewsOne.html");
            if (!isset($_COOKIE["username"])) {
               echo
               "<h1><a href='HW14Form.php?pageNews=HW14NewsOne.html'>
               Attack on Titan Final Season Part 3 Ending Soon!
               </a></h1>
               <h1><a href='HW14Form.php?pageNews=HW14NewsTwo.html'>
               Demon Slayer: Kimetsu No Yaiba Officially Ended
               </a></h1>
               <h1><a href='HW14Form.php?pageNews=HW14NewsThree.html'>
               Pokemon on its Seventh Series!
               </a></h1>
               <h1><a href='HW14Form.php?pageNews=HW14NewsFour.html'>
               One of the Longest Anime of All Times: Doraemon
               </a></h1>
               <h1><a href='HW14Form.php?pageNews=HW14NewsFive.html'>
               Sports Anime Of All Times
               </a></h1>";
            }
            else {
               echo
               "<h1><a href='HW14NewsOne.html'>
               Attack on Titan Final Season Part 3 Ending Soon!
               </a></h1>
               <h1><a href='HW14NewsTwo.html'>
               Demon Slayer: Kimetsu No Yaiba Officially Ended
               </a></h1>
               <h1><a href='HW14NewsThree.html'>
               Pokemon on its Seventh Series!
               </a></h1>
               <h1><a href='HW14NewsFour.html'>
               One of the Longest Anime of All Times: Doraemon
               </a></h1>
               <h1><a href='HW14NewsFive.html'>
               Sports Anime Of All Times
               </a></h1>";
            }
         ?>
      </div>
   </div>
</body>