<?php

require '/core/mysql.class.php';
$conn    = Connect();
$date    = $_POST['date'];
$title   = $_POST['title'];
$description   = $_POST['description'];
$query   = "INSERT INTO calendar (date, title, description) VALUES ('$date','$title', '$description')";
$success = $conn->query($query);

if (!$success) {
    die($conn->error);

}

$conn->close();

echo "Event added, click <a href='http://localhost'>here</a> to see it";

?>
