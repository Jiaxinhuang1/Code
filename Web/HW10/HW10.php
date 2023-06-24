<?php
	error_reporting(E_ALL);
	$CorrectAnswers = 0;
	$isCorrect3 = false;
	$isCorrect4 = false;
	$Answer1 = $_POST['Question1'];
	$Answer2 = $_POST['Question2'];
	$Answer3 = $_POST['Question3'];
	$Answer4 = $_POST['Question4'];
	$Answer5 = trim($_POST['Question5']);
	$Answer6 = trim($_POST['Question6']);
	if ($Answer1 == "false"){
		echo "Correct";
		$CorrectAnswers ++;
	}
	if ($Answer2 == "true"){
		echo "Correct2";
		$CorrectAnswers ++;
	}
	foreach ($Answer3 as $answer4) {
		if ($answer4 == "b") {
			$isCorrect3 = true;
		} 
		else {
			$isCorrect3 = false;
			break;
		}
	}
	if ($isCorrect3) {
		echo "Correct3";
		$CorrectAnswers ++;
	}
	foreach ($Answer4 as $answer4) {
		if ($answer4 == "c") {
			$isCorrect4 = true;
		} 
		else {
			$isCorrect4 = false;
			break;
		}
	}
	if ($isCorrect4) {
		echo "Correct4";
		$CorrectAnswers ++;
	}
	if (strtolower($Answer5) == "http"){
		echo "Correct5";
		$CorrectAnswers++;
	}
	if (strtolower($Answer6) == "favicon"){
		echo "Correct6";
		$CorrectAnswers++;
	}
	echo 
		'<script type="text/javascript">
			alert("Your Grade is '.$CorrectAnswers.' / 6.");
			location.href = "HW10.html";
		</script>';
?>