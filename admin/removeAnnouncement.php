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
$query   = "DELETE FROM noticebar";

$success = $conn->query($query);

if (!$success) {
    die("Couldn't enter data: ".$conn->error);

}

$conn->close();

echo 'Event removed, click <a href="/index.php">here</a> to see it '

?>
