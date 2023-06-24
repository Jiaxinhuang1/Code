<?php
 session_start();
 $username = $_SESSION["username"];
 //echo $username . "<br>";
 //$results = fopen("results.txt", "w");
 //$results_array = file("results.txt");
 //foreach ($results_array as $result) {
 //	$results_list[] = explode(":", $result);
 //}
 //print_r($results_list);
 //$current = $_SESSION["username"] . ":" . $_SESSION["score"];
 //fwrite($results, $current . "\n");
 //fclose($results)
 

 if ($_POST["page"] == "DoneQ1")
 {
   if ($_POST['Question1'] == "false") {
	$_SESSION["score"] = $_SESSION["score"] + 10;
	//echo $_SESSION["score"];
	//fwrite($results, $_SESSION["score"]);
   }
   DisplayQ2();
 }
 elseif ($_POST["page"] == "DoneQ2")
 {
   if ($_POST['Question2'] == "true") {
	$_SESSION["score"] = $_SESSION["score"] + 10;
	//echo $_SESSION["score"];
   }
   DisplayQ3();
 }
 elseif ($_POST["page"] == "DoneQ3")
 {
   foreach ($_POST['Question3'] as $answer3) {
	if ($answer3 == "b") {
		$isCorrect3 = true;
	} 
	else {
		$isCorrect3 = false;
		break;
	}
   }
   if ($isCorrect3) {
	$_SESSION["score"] = $_SESSION["score"] + 10;
	//echo $_SESSION["score"];
   }
   DisplayQ4();
 }
 elseif ($_POST["page"] == "DoneQ4")
 {
   foreach ($_POST['Question4'] as $answer4) {
	if ($answer4 == "c") {
		$isCorrect4 = true;
	} 
	else {
		$isCorrect4 = false;
		break;
	}
   }
   if ($isCorrect4) {
	$_SESSION["score"] = $_SESSION["score"] + 10;
	//echo $_SESSION["score"];
   }
   DisplayQ5();
 }
 elseif ($_POST["page"] == "DoneQ5")
 {
   if (strtolower($_POST['Question5']) == "http"){
	$_SESSION["score"] = $_SESSION["score"] + 10;
	//echo $_SESSION["score"];
   }
   DisplayQ6();
 }
 elseif ($_POST["page"] == "DoneQ6")
 {
   if (strtolower($_POST['Question5']) == "favicon"){
	$_SESSION["score"] = $_SESSION["score"] + 10;
	//echo $_SESSION["score"];
   }
   DisplayResult();
   //fclose($results);
 }
 else
 {
    DisplayQ1();
 }

 function DisplayQ1()
 {
  $script = $_SERVER['PHP_SELF'];
  print <<<QUESTION1
  <html>
  <head>
  	<title> Quiz </title>
  	<link href="HW15.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "quiz" method = "post" action = "$script">
  	<h1> Question 1 </h1>
  	<div><h3>"URL" stands for "Universal Reference Link".</h3></div>
	<div>
		<input name = "Question1" type = "radio" value = "true"/>
		<label> a) True </label>
	</div>
	<div>
		<input name = "Question1" type = "radio" value = "false"/>
		<label> b) False </label>
	</div>
	<div>
		<input type = "hidden" name = "page" value = "DoneQ1" />
		<input type = "submit" value = "Next" class = "button"/>
	</div>
  </form>
  </body>
  </html>
QUESTION1;
  }

 function DisplayQ2()
 {
  $script = $_SERVER['PHP_SELF'];
  print <<<QUESTION2
  <html>
  <head>
  	<title> Quiz </title>
  	<link href="HW15.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "quiz" method = "post" action = "$script">
  	<h1> Question 2 </h1>
  	<div><h3>An Apple MacBook is an example of a Linux system.</h3></div>
	<div>
		<input name = "Question2" type = "radio" value = "true"/>
		<label> a) True </label>
	</div>
	<div>
		<input name = "Question2" type = "radio" value = "false"/>
		<label> b) False </label>
	</div>
	<div>
		<input type = "hidden" name = "page" value = "DoneQ2" />
		<input type = "submit" value = "Next" class = "button"/>
	</div>
  </form>
  </body>
  </html>
QUESTION2;
  }

 function DisplayQ3()
 {
  $script = $_SERVER['PHP_SELF'];
  print <<<QUESTION3
  <html>
  <head>
  	<title> Quiz </title>
  	<link href="HW15.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "quiz" method = "post" action = "$script">
  	<h1> Question 3 </h1>
  	<div><h3>Which of these do NOT contribute to packet delay in a packet switching network?</h3></div>
	<div>
		<input name = "Question3[]" type = "checkbox" value = "a"/>
		<label> a) Processing delay at a router </label>
	</div>
	<div>
		<input name = "Question3[]" type = "checkbox" value = "b"/>
		<label> b) CPU workload on a client </label>
	</div>
	<div>
		<input name = "Question3[]" type = "checkbox" value = "c"/>
		<label> c) Transmission delay along a communications link </label>
	</div>
	<div>
		<input name = "Question3[]" type = "checkbox" value = "d"/>
		<label> d) Propagataion delay </label>
	</div>
	<div>
		<input type = "hidden" name = "page" value = "DoneQ3" />
		<input type = "submit" value = "Next" class = "button"/>
	</div>
  </form>
  </body>
  </html>
QUESTION3;
  }

 function DisplayQ4()
 {
  $script = $_SERVER['PHP_SELF'];
  print <<<QUESTION4
  <html>
  <head>
  	<title> Quiz </title>
  	<link href="HW15.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "quiz" method = "post" action = "$script">
  	<h1> Question 4 </h1>
  	<div><h3>The Internet layer is responsible for creating the packets that move across the network.</h3></div>
	<div>
		<input name = "Question4[]" type = "checkbox" value = "a"/>
		<label> a) Physical </label>
	</div>
	<div>
		<input name = "Question4[]" type = "checkbox" value = "b"/>
		<label> b) Data Link </label>
	</div>
	<div>
		<input name = "Question4[]" type = "checkbox" value = "c"/>
		<label> c) Network </label>
	</div>
	<div>
		<input name = "Question4[]" type = "checkbox" value = "d"/>
		<label> d) Transport </label>
	</div>
	<div>
		<input type = "hidden" name = "page" value = "DoneQ4" />
		<input type = "submit" value = "Next" class = "button"/>
	</div>
  </form>
  </body>
  </html>
QUESTION4;
  }

 function DisplayQ5()
 {
  $script = $_SERVER['PHP_SELF'];
  print <<<QUESTION5
  <html>
  <head>
  	<title> Quiz </title>
  	<link href="HW15.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "quiz" method = "post" action = "$script">
  	<h1> Question 5 </h1>
  	<div>
		<h3><input name = "Question5" type = "text" size = "10"/>
		is a networking protocol that runs over TCP/IP, and governs communication between web browsers and web servers.</h3>
	</div>
	<div>
		<input type = "hidden" name = "page" value = "DoneQ5" />
		<input type = "submit" value = "Next" class = "button"/>
	</div>
  </form>
  </body>
  </html>
QUESTION5;
  }

 function DisplayQ6()
 {
  $script = $_SERVER['PHP_SELF'];
  print <<<QUESTION6
  <html>
  <head>
  	<title> Quiz </title>
  	<link href="HW15.css" rel="stylesheet">
  </head>
  <body>
  	<form class = "quiz" method = "post" action = "$script">
  	<h1> Question 6 </h1>
  	<div>
		<h3>A small icon displayed in a browser table that identifies a website is called a 
		<input name = "Question5" type = "text" size = "10"/>.</h3>
	</div>
	<div>
		<input type = "hidden" name = "page" value = "DoneQ6" />
		<input type = "submit" value = "Next" class = "button"/>
	</div>
  </form>
  </body>
  </html>
QUESTION6;
  }

 function DisplayResult()
 {
  echo 
	"<head>
		<title>Quiz Result</title>
		<link href='HW15.css' rel='stylesheet'>
	</head>
	<body>
		<div class = 'quiz'>
			<h1>" . $_SESSION["username"] . " scored " . $_SESSION["score"] . " out of 60 </h1>
			<a href='HW15.php' class = 'button'>Return Back to Login</a>
		</div>
	</body>";  
}

?>