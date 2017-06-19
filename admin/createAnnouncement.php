<?php

function Connect()
{
require '/scripts/password.php';

 // Create connection
 $conn = new mysqli($servername, $username, $password, $dbname) or die($conn->connect_error);

 return $conn;
}

$conn    = Connect();
$icon    = $_POST['icon'];
$notice = $_POST['notice'];
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
