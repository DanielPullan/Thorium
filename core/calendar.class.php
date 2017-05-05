<?php

require_once('\core\mysql.class.php');
// Create connection
$conn = mysqli_connect($host, $user, $pass, $db);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

    $sql = "SELECT id, title, description, date FROM calendar";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo "<li><p class='calendarTextHead'>" . $row["title"] . "</p> <p class='calendarTextDate'>" . $row["date"] . "</p> <p class='calendarText'>" . $row["description"] . "</p>" . " ";
    }
} else {
    echo "0 results";
}

mysqli_close($conn);

?>
