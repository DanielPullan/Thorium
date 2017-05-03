<?php

require 'connect.php';
$conn    = Connect();
$date    = $_POST['date'];
$title   = $_POST['title'];
$description   = $_POST['description'];
$query   = "DELETE FROM calendar WHERE title='".$title."'";
$success = $conn->query($query);

if (!$success) {
    die("Couldn't enter data: ".$conn->error);

}

$conn->close();

echo 'Event added, click <a href="http://localhost">here</a> to see it '

?>
