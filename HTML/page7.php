<html>
<head>
    <link rel="stylesheet" href="../hero.css">
    <link rel="stylesheet" href="https://use.typekit.net/uef6xit.css">
    <link rel="stylesheet" href="page2.css">
</head>
<body>
    
    <div id="background1"></div>
    <div id="header">
        <a href="index.php">
            <img id="headerimage" src="../images/GameTimeLight.png" href="index.html" align="middle">
        </a>
        <?php
    $first = $_POST["FirstGame"];
    $second = $_POST["SecondGame"];
    $third = $_POST["ThirdGame"];
    $command = escapeshellcmd("python gametime.py $first $second $third");
    $output = exec($command);
    echo "<p style='font-family: aglet-slab; font-size: 90px; padding: 100px; color: white;'>".$output."</p>";

    ?>
    </div>
</body>
</html>