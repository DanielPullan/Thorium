<head>
    <title>Thorium Admin</title>
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/simple-grid.css">
    <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<div class="row header">
    <div class="col-7">
        <h1><i class="fa fa-cog fa"></i>Thorium Admin Panel</h1>
        <p>What would you like to do today?</p>
    </div>
</div>

<?php $output = shell_exec('python kill-the-pi.py');
echo "<pre>$output</pre>";
?>

<div class="row">
    <div class="col-3 box">
        <h3>
            <a href="/manageSite"><i class="fa fa-globe fa"></i>Manage site</a>
        </h3>
        <p>
            Manage details and style of your digital signage.
        </p>
    </div>
    <div class="col-3 box">
        <h3>
            <a href="/gallery"><i class="fa fa-image fa"></i>Gallery
        </h3></a>
        <p>
            Make changes to the slider or uploaded images
        </p>
    </div>
    <div class="col-3 box">
        <h3>
            <a href="/calendar"><i class="fa fa-calendar fa"></i>Calendar</a>
        </h3>
        <p>
            Add or remove events from your calendar
        </p>
    </div>
    <div class="col-3 box">
        <h3>
            <i class="fa fa-sitemap fa"></i>Clients
        </h3>
        <p>
            Manage your clients and export data
        </p>
    </div>
</div>

<div class="row">
    <div class="col-3 box">
        <h3>
            <a href="/socialMedia"><i class="fa fa-external-link fa"></i>Social Media</a>
        </h3>
        <p>
            Manage the links to your social media feeds
        </p>
    </div>
    <div class="col-3 box">
        <h3>
            <a href="/banner"><i class="fa fa-map-signs fa"></i>Banner</a>
        </h3>
        <p>
            Show, hide or make changes to your banner
        </p>
    </div>
    <div class="col-3 box">
        <h3>
            <a href="/calendar"><i class="fa fa-terminal fa"></i>Terminal</a>
        </h3>
        <p>
            Run commands on the server within your browser
        </p>
    </div>
    <div class="col-3 box">
        <h3>
            <i class="fa fa-server fa"></i>Server
        </h3>
        <p>
            View your server status and monitor information
        </p>
    </div>
</div>
