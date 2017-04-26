<!DOCTYPE HTML>
<html>
<head>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<style>
.thumb{border:2px dotted #eee;padding:3px;width:100px;}.thumb:hover{border:2px dotted gray;}
</style>
</head>
<body>
<div class="photo-upload">
  <form action="index.php" method="POST"  enctype="multipart/form-data">
		<input type="file" name="photo" value="browse" id="photo"/>
		<input type="submit" name="send" value="Upload" id="post" />
	</form>
</div>
<?php
	include 'upload.class.php';
	$size    = 300;
	$dir =   'uploads/';
	$newdir= 'resized/';
	$img = $upload->photoUpload();
	$max_w = 150;
	$max_h = 150;
	$th_w = 100;
	$th_h = 100;
	$upload->resizejpeg($dir, $newdir, $img, $max_w, $max_h, $th_w, $th_h);
  echo '<br />';
  echo '<div class="thumb">';
		echo $upload->dumpPhoto($img,$newdir);
	echo '</div>'
?>
</body>
</html>
