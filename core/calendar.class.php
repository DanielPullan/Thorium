<?php

require_once('\core\mysql.class.php');
// Create connection


$stmt = $pdo->query('SELECT id, title, description, date FROM calendar');
while ($row = $stmt->fetch())
{
    echo "<li><p class='calendarTextHead'>" . $row["title"] . "</p> <p class='calendarTextDate'>" . $row["date"] . "</p> <p class='calendarText'>" . $row["description"] . "</p>" . " ";
}



