<?php
if(isset($_POST['facebook']) && isset($_POST['twitter'])) {
    $data = "<li><p class='calendarText'>"." ".$_POST['facebook'] . "</p><p class='calendarText'>" . $_POST['twitter'] ."</p></li>". "\n";
    $ret = file_put_contents('socialData.php', $data, LOCK_EX);
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
