 <!DOCTYPE html>
 <html lang="en">

 <head>
   <meta charset="utf-8">
   <meta name="author" content="Group-32, Fall 2021">
   <meta name="viewport" content="width=device-width,initial-scale=1">
   <title>S.R.I.J.A.S - Login</title>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
   <link rel="stylesheet" href="css/style.css">
 </head>

 <head>
   <meta name="viewport" content="width=device-width, initial-scale=1">
 </head>

 <body>

   <div class="header">
     <img src="logo.jpg" alt="logo">
     <div class="header-right">
       <a class="active" href="home.php">Home</a>
       <a href="register.php">Register</a>
       <a href="logout.php">Logout</a>
     </div>
   </div>

 </body>
 <?php
  session_start();
  if (!isset($_SESSION['user'])) {
    header('Location: login.php');
  }
  include "connectDB.php";
  $user_email = $_SESSION['user'];
  $user = $user_email;
  // echo "User Job Boards";
  $userJbQuery = "select jb.name, jb.job_board_id from job_board jb, user_notification un, user_master um where jb.job_board_id = un.job_board_id and un.user_id = um.user_id and um.user_email = '" . $user_email . "'";
  $userJbResult = $conn->query($userJbQuery);
  $job_board_array = array();
  $job_board_ids = array();
  while ($row = $userJbResult->fetch_assoc()) {
    array_push($job_board_array, $row["name"]);
    array_push($job_board_ids, $row["job_board_id"]);
    // echo $job_board_array[0];
    // echo "<br>";
  }
  ?>

 <body>
   <div class="bg">
     <section class="h-100">
       <div class="container h-100">
         <div class="row justify-content-sm-center h-100">
           <div class="col-xxl-4 col-xl-5 col-lg-5 col-md-7 col-sm-9">
             <div class="text-center my-5">
             </div>

             <div class="card shadow-lg">
               <div class="card-body p-5">
                 <h1 class="fs-4 card-title fw-bold mb-4">Registered Job Boards</h1>
                 <form method="POST" action="" class="needs-validation" novalidate="" autocomplete="off">

                   <?php
                    foreach ($job_board_array as $jb) {
                      echo "<div class='mb-3'>";
                      echo "<label class='mb-2'>" . $jb . "</label>";
                      echo "</div>";
                    }
                    ?>
                   <div>
                     <!-- Display User Details -->
                     <?php
                      include('connectDB.php');

                      $sqlget   = "SELECT * FROM user_master";
                      $sqldata  = mysqli_query($conn, $sqlget) or die('Error retrieving data');
                      
                      echo "<table>";
                      echo "<tr><th>First Name</th><th>Last Name</th><th>Email</th></tr>";

                      while($row = mysqli_fetch_array($sqldata, MYSQLI_ASSOC)) {
                        echo "<tr><td>";
                        echo $row['user_fname'];
                        echo "</td><td>";
                        echo $row['user_lname'];
                        echo "</td><td>";
                        echo $row['user_email'];
                        echo "</td></tr>";
                      }
                      ?>

                   </div>
                   <div>
                     <!-- Button for updating resume -->
                     <?php
                      if (isset($_POST['submit'])) {
                        header("Location: updateResume.php");
                        exit;
                      }
                      ?>

                     <button type="submit" name="updateResume" align="left" class="btn btn-primary ms-auto"> Update Resume </button>

                     <!-- Button for Delete Account -->
                     <?php
                      if (isset($_POST['submit'])) {
                        header("Location: deleteAccount.php");
                        exit;
                      }
                      ?>

                     <button type="submit" name="deleteAccount" align="center" class="btn btn-primary ms-auto"> Delete Account </button>
                   </div>
               </div>
             </div>
           </div>
           </form>

         </div>
         <br>
         <div align="center">Made with <span style="color: #e25555;">&hearts;</span>. Contribute on <a href="https://github.com/sak007/SRIJAS" class="text-dark" target="_blank">GitHub</a>.</div>
         <br>
       </div>
 </body>

 </html>