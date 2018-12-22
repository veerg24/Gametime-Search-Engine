<!DOCTYPE html>
<html>
<br><br><br>
<center>
    

<?php
    $first = $_POST["FirstGame"];
    $second = $_POST["SecondGame"];
    $third = $_POST["ThirdGame"];
    $command = escapeshellcmd("python gametime.py $first $second $third");
    $output = shell_exec($command);
    echo $output;

?>
<div id="header">
    <a href="index.php">
        <img id="headerimage" src="../images/GameTimeLight.png" href="index.html" align="middle">
    </a>
</div>
<br><br><br><br>
<head>
    <link rel="stylesheet" href="page6.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.loader {
  border: 12px solid #f3f3f3;
  border-radius: 50%;
  border-top: 12px solid blue;
  border-bottom: 12px solid turquoise;
  width: 350px;
  height: 350px;
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}

@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
stop()
</style>
</head>
<body>
<div class="loader"></div>
<br><br><br><br><br>
<h2>If this page doesn't direct you automatically, please</h2>
    
<a href="page7.php" id="clickhere">Click Here</a>
<br><br><br><br><br><br><br><br><br><br><br><br>

</body>
</center>
</html>