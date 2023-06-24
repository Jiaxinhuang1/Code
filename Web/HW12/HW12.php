<!DOCTYPE html>

<html lang="en">

<head>
   <title>HW12</title>
   <meta charset="UTF-8">
   <meta name="description" content="Online Signup Sheet with PHP">
   <meta name="author" content="Jiaxin Huang">
   <style>
      body {
         background-color: #DCD9C2;
      }
      h1 {
         font-size: 40pt;
	 font-weight: bold;
         font-variant: small-caps;
	 text-align: center;
      }
      table {
         margin: auto;
	 padding: 10px;
	 width: 50%;
	 border: 3px solid black;
      }
      th {
	 text-align: center;
	 font-size: 25pt;
         background-color: #CCD6B8;
      }	
      td {
         text-align: center;
	 font-size: 20pt;
      }
      input {
         border: 2px solid black;
	 width: 50%;
	 height: 100%;
      }
      .button {
	 width: 30%;
	 height: 10%;
         position: relative;
	 margin-top: 10px;
	 left: 35%;
         padding: 5px;
         font-size: 30pt;
         background-color: #E2ECCB;
      }
      .button:hover {
         background-color: #EDF0E6;
      }
      .button:active {
         background-color: #959595;
      }
   </style>
</head> 
<body>
   <?php
      // opens file and assigns slot variables
      $file = fopen('signup.txt', 'r');
      $Slot1 = $_POST['Slot1'];
      $Slot2 = $_POST['Slot2'];
      $Slot3 = $_POST['Slot3'];
      $Slot4 = $_POST['Slot4'];
      $Slot5 = $_POST['Slot5'];
      $Slot6 = $_POST['Slot6'];
      $Slot7 = $_POST['Slot7'];
      $Slot8 = $_POST['Slot8'];
      $Slot9 = $_POST['Slot9'];
      $Slot10 = $_POST['Slot10'];

      // gets first line of file and divide into arrays separated by ,
      $string = fgets($file);
      $array = explode(",", $string);
      fclose($file);

      // create empty array to store current status
      $arr = array();
      $file = fopen('signup.txt', 'w'); 

      // if the current slot is not empty set the array at slot position as value
      // if the current slot is empty set the array with what is saved in file at that position  
      if (!empty($Slot1)){
         $arr[0] = $Slot1;
      }
      else {
         $arr[0] = $array[0];
      }
      if (!empty($Slot2)){
         $arr[1] = $Slot2;
      }
      else {
         $arr[1] = $array[1];
      }

      if (!empty($Slot3)){
         $arr[2] = $Slot3;
      }
      else {
         $arr[2] = $array[2];
      }

      if (!empty($Slot4)){
         $arr[3] = $Slot4;
      }
      else {
         $arr[3] = $array[3];
      }

      if (!empty($Slot5)){
         $arr[4] = $Slot5;
      }
      else {
         $arr[4] = $array[4];
      }

      if (!empty($Slot6)){
         $arr[5] = $Slot6;
      }
      else {
         $arr[5] = $array[5];
      }

      if (!empty($Slot7)){
         $arr[6] = $Slot7;
      }
      else {
         $arr[6] = $array[6];
      }

      if (!empty($Slot8)){
         $arr[7] = $Slot8;
      }
      else {
         $arr[7] = $array[7];
      }

      if (!empty($Slot9)){
         $arr[8] = $Slot9;
      }
      else {
         $arr[8] = $array[8];
      }

      if (!empty($Slot10)){
         $arr[9] = $Slot10;
      }
      else {
         $arr[9] = $array[9];
      }

      // write the new array that combines old and new data to the file
      foreach ($arr as $lin) {
         fwrite($file, $lin.",");
      }
      fclose($file);
   ?>

   <h1>Sign-Up Sheet</h1>
   <form id = "Signup" method = "POST" action = "HW12.php">
      <table border = "3px">
         <tr>
            <th>Time</th>
            <th>Name</th>
         </tr>
         <tr>
            <td>8:00 am</td>
            <td><?php 
               // if the current array is empty then input field else print what is saved
               if (empty($arr[0])){
                  print '<input name = "Slot1" type = "text" size = "30">';
               }
               else {
                  print $arr[0];
               }

               //fclose($file); 
            ?></td>
         </tr>
         <tr>
            <td>9:00 am</td>
            <td><?php
               if (empty($arr[1])){
                  print '<input name = "Slot2" type = "text" size = "30">';
               }
               else {
                  print $arr[1];
               }

            ?></td>
         </tr>
         <tr>
            <td>10:00 am</td>
            <td><?php
               if (empty($arr[2])){
                  print '<input name = "Slot3" type = "text" size = "30">';
               }
               else {
                  print $arr[2];
               }

            ?></td>
         </tr>
         <tr>
            <td>11:00 am</td>
            <td><?php
               if (empty($arr[3])){
                  print '<input name = "Slot4" type = "text" size = "30">';
               }
               else {
                  print $arr[3];
               }

            ?></td>
         </tr>
         <tr>
            <td>12:00 pm</td>
            <td><?php
               if (empty($arr[4])){
                  print '<input name = "Slot5" type = "text" size = "30">';
               }
               else {
                  print $arr[4];
               }
            ?></td>
         </tr>
         <tr>
            <td>1:00 pm</td>
            <td><?php
               if (empty($arr[5])){
                  print '<input name = "Slot6" type = "text" size = "30">';
               }
               else {
                  print $arr[5];
               }
            ?></td>
         </tr>
         <tr>
            <td>2:00 pm</td>
            <td><?php
               if (empty($arr[6])){
                  print '<input name = "Slot7" type = "text" size = "30">';
               }
               else {
                  print $arr[6];
               }

            ?></td>
         </tr>
         <tr>
            <td>3:00 pm</td>
            <td><?php
               if (empty($arr[7])){
                  print '<input name = "Slot8" type = "text" size = "30">';
               }
               else {
                  print $arr[7];
               }
            ?></td>
         </tr>
         <tr>
            <td>4:00 pm</td>
            <td><?php
               if (empty($arr[8])){
                  print '<input name = "Slot9" type = "text" size = "30">';
               }
               else {
                  print $arr[8];
               }
            ?></td>
         </tr>
         <tr>
            <td>5:00 pm</td>
            <td><?php
               if (empty($arr[9])){
                  print '<input name = "Slot10" type = "text" size = "30">';
               }
               else {
                  print $arr[9];
               }
            ?></td>
         </tr>
      </table>
      <input type="submit" value="Submit" class="button">
   </form>
</body>
</html>