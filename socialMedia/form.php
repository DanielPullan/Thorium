<?php
if(isset($_POST['facebook']) && isset($_POST['twitter'])) {
    $data = "<li><p><i class='fa fa-facebook fa'></i>"." ".$_POST['facebook'] . "</p></li><li><p><i class='fa fa-twitter fa'></i>" . $_POST['twitter'] ."</p></li>". "\n";
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
