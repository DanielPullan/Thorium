<?php
if(isset($_POST['field1']) && isset($_POST['field2'])) {
    $data = "<li><p class='calendarText'>"." ".$_POST['field1'] . "</p><p class='calendarText'>" . $_POST['field2'] ."</p></li>". "\n".
    "<li><p class='calendarText'>"." ".$_POST['field3'] . "</p><p class='calendarText'>" . $_POST['field4'] ."</p></li>". "\n".
    "<li><p class='calendarText'>"." ".$_POST['field5'] . "</p><p class='calendarText'>" . $_POST['field6'] ."</p></li>". "\n".
    "<li><p class='calendarText'>"." ".$_POST['field7'] . "</p><p class='calendarText'>" . $_POST['field8'] ."</p></li>". "\n".
    "<li><p class='calendarText'>"." ".$_POST['field9'] . "</p><p class='calendarText'>" . $_POST['field10'] ."</p></li>". "\n";
    $ret = file_put_contents('calendarData.php', $data, LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
    }
}
else {
   die('no post data to process');
}
?>
