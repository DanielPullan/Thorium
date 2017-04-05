
<head>
    <title>Localhost - Thoriums</title>
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/simple-grid.css">
    <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<?php


    $xml = simplexml_load_file('sampleData.xml');

// thanks madison for showing me how to make this bit work
    foreach($xml->children() as $image) {
        echo "<li>
                <img src='".$image->link."' />
            </li>";
    }
    ?>
