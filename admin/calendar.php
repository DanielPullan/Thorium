<?php
$servername = "localhost";
$username = "root";
$password = "1123";
$dbname = "Thorium";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

    $sql = "SELECT id, title, description FROM calendar";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo "<li><p class='calendarText'>" . $row["title"] . "</p> <p class='calendarText'>" . $row["description"] . "</p>" . "<br>";
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?>
