<!DOCTYPE html>

<html lang="en">

<head>
   <title>HW14Form</title>
   <meta charset="UTF-8">
   <meta name="description" content="Newspaper Login Using Cookies">
   <meta name="author" content="Jiaxin Huang">
   <link href="HW14.css" rel="stylesheet">
</head>
<body id="formbg">
   <form id = "login" method = "POST" action = "HW14Form.php">
      <table>
         <tr>
            <th colspan="2" style="font-size:24pt">User Login</th>
         </tr>
         <tr>
            <td>Username: </td>
            <td><input name = "username" type = "text" size = "30"></td>
         </tr>
         <tr>
            <td>Password: </td>
            <td><input name = "password" type = "password" size = "30"></td>
         </tr>
         <tr>
          <td colspan="2"><input type = "submit" value = "Login" name = "login" class = "button"></td>
         </tr>
         <?php
            setcookie("page", $_GET["pageNews"]);
            $file = fopen("329E.passwd.txt", "r");
            // make one array with each line as index item
            $file_array = file("329E.passwd.txt");
            // make into 2D array [[user, pass], [user, pass]]
            foreach ($file_array as $user) {
               $users[] = explode(':', $user);
            }
            //print_r($users);
            fclose($file);
            if (!empty($_POST['login'])) {
               $username = trim($_POST['username']);
               $password = trim($_POST['password']);
               $login = false;
               //print("What is Typed: " . $username . " , " . $password);
               foreach ($users as $user) {
                  if ($username == trim($user[0]) && $password == trim($user[1])) {
                     //print($user[0] . " , " . $user[1]);
                     $login = true;
                     setcookie("username", $username, time() + 120);
                     setcookie("password", $password, time() + 120);
                     header("Location: ".$_COOKIE["page"]);
                     echo "<tr><td colspan='2' style='text-align: center'>Successful Login</td></tr>";
                     break;
                  }
               }
               if (!$login) {
		  setcookie("page", "HW14NewsOne.html");
                  echo "<tr><td colspan='2' style='text-align: center'>Username or Password is not Valid</td></tr>";
               }
            }
         ?>
      </table>
   </form>
</body>
</html>
