<?php
if(isset($_POST['icon']) && isset($_POST['banner'])) {
    $data = "<p class='panelText'><i class='" . $_POST['icon'] . "'></i>" . $_POST['banner'] ."</p>". "\n";
    $ret = file_put_contents('bannerData.php', $data, LOCK_EX);
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
