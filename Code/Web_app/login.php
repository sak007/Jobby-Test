<html lang="en">
<head>

<!-- We use Bootstrap CSS for styling purposes-->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<style media="screen">
  input[type="email"]::placeholder {
      text-align: center;
  }
  input[type="password"]::placeholder {
      text-align: center;
  }
</style>
<title> S.R.I.J.A.S. </title>
</head>
<body>
<!-- Here, we create a simple form with the options to add name, email, job type and upload a .pdf file-->
  <div style="background: url(https://i.postimg.cc/3N7wnb75/background.jpg)no-repeat; background-size: cover;" class="jumbotron bg-cover text-white">
      <div class="container py-5 text-center">
          <h1 class="display-4 font-weight-bold">S.R.I.J.A.S. (Smart Resume Interpreter And Job Alerts System)</h1>
      </div>
  </div>

<div class="align-items-center" align = "center">
  <form method="post" action="">

    <div class="form-group  col-4">
      <label for="inputEmail">Email address</label>
      <input type="email" name="inputEmail" class="form-control" id="inputEmail" placeholder="Enter email" required>
    </div>

    <div class="form-group  col-4">
      <label for="inputLocation">Password</label>
      <input type="password" name="password" class="form-control" id="password" placeholder="Enter password" required>
    </div>

    <div class="col-auto my-1">
      <button type="submit" value="Submit" id="submit" name="submit" class="btn btn-primary col-auto">Login</button>
    </div>
  </form>
  <?php
   if(isset($_POST['submit']) && ($_POST['inputEmail'] != "") && ($_POST['password'] != "")){
     session_start();
     $paramsFile = file_get_contents("parameters.json");
     $params = json_decode($paramsFile, true);
     $servername = $params["server_name"];
     $username = $params["user_name"];
     $password = $params["password"];
     $db = $params["db_name"];
    $conn = new mysqli($servername, $username, $password, $db);
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }
    $sql = "SELECT user_pwd FROM user_master where user_email='".$_POST['inputEmail']."'";
    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
    $len = $result->num_rows;
    if (($len == 1) && ($row["user_pwd"] == $_POST['password'])) {
        $_SESSION['user'] = $_POST['inputEmail'];
        header('Location: home.php');
    } else {
      echo '<span style="color:#FF0000"> Invalid Email/Password </span><br/>';
    }
    $conn->close();
  }
  ?>
  <a href="signup.php">New User? Click here to Sign Up<a/>
</div>
<!-- Here, we add a link to a useful resource for job searches-->
<div class="container hero">
    <div class="row">
        <div class="col-md-8 offset-md-2">
            <h1 class="text-center">Job Search Was Never This Easy!</h1>
            <h4 class="text-center"> Wake up to email updates about what happened in the last one day, and get up to speed with applying for that dream job.</h4>
            <div class="embed-responsive embed-responsive-16by9"><iframe width="560" height="315" src="https://www.youtube.com/embed/u75hUSShvnc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
        </div>
    </div>
</div>
<br>
<div align="center">Made with <span style="color: #e25555;">&hearts;</span>. Contribute on GitHub.</div>
<br>
<br>
<br>
<br>
</body>
</html>
