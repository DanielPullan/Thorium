<?php

function Connect()
{
require __DIR__.'/../scripts/password.php';

 // Create connection
 $conn = new mysqli($servername, $username, $password, $dbname) or die($conn->connect_error);

 return $conn;
}

$conn    = Connect();
$icon    = $conn->real_escape_string($_POST['icon']);
$notice = $conn->real_escape_string($_POST['notice']);
$query   = "UPDATE noticebar SET icon='$icon', notice='$notice' WHERE ID='7'";

//"INSERT INTO noticebar (icon, notice) VALUES ('$icon','$notice')";

// "UPDATE noticebar SET icon=$icon, notice=$notice WHERE ID='7'"
$success = $conn->query($query);

if (!$success) {
    die("Couldn't enter data: ".$conn->error);

}

$conn->close();

echo 'Banner added, click <a href="http://localhost">here</a> to go to Digital Signage '

?>
