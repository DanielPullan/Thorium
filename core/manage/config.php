<?php
// Configuration file for Krypton \\

	//Server configuration (Database connection!)
	$_CONFIG['mysql']['host'] = 'localhost'; //The IP for the datebase server
	$_CONFIG['mysql']['user'] = 'root'; //The username for the database server
	$_CONFIG['mysql']['pass'] = '1123'; //The password for the datebase server
	$_CONFIG['mysql']['db'] = 'Thorium'; //Select the database you want to connect too
	//Site Configuration
	$_CONFIG['site']['url'] = 'http://localhost'; //Server URL example.com (DOES NOT END WITH /)
	$_CONFIG['site']['name'] = 'Poole High School'; //Website name, {SITE_NAME}
	$_CONFIG['site']['template'] = 'Thorium'; //Krypton Template System, Select the Template Directory
	$_CONFIG['site']['tw'] = 'poole_high'; //Your website Twitter profile link
	$_CONFIG['site']['fb'] = 'poolehs'; //Your website facebook page link
	$_CONFIG['site']['twapi'] = 'https://twitter.com/poole_high'; //Your website twitter API
	$_CONFIG['site']['banner'] = "<p class='panelText'><i class='fa fa-bell-slash fa'></i>Look, I won the no-bell prize</p>";
	$_CONFIG['site']['date'] = "<p style='text-align:right' id='date'></p>"
?>
