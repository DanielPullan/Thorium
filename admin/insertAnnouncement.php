<?php

function Connect()
{
 $dbhost = "localhost";
 $dbuser = "root";
 $dbpass = "1123";
 $dbname = "thorium";

 // Create connection
 $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname) or die($conn->connect_error);

 return $conn;
}

$conn    = Connect();
$icon    = $_POST['icon'];
$notice = $_POST['notice'];
$query   = "INSERT INTO noticebar (icon, notice) VALUES ('$icon','$notice')";
$success = $conn->query($query);

if (!$success) {
    die("Couldn't enter data: ".$conn->error);

}

$conn->close();

echo 'Event added, click <a href="http://localhost">here</a> to see it '

?>
