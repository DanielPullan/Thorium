<html>

<head>
    <title>{SITE_NAME}</title>
    <link rel="stylesheet" href="{URL}/template/{TPL}/style.css">
    <link rel="stylesheet" href="{URL}/template/{TPL}/simple-grid.css">
    <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>

  <div class="row header">
      <div class="col-7">
          <h1 class="headerText"><img src="/assets/logo.png" /></h1>
      </div>
      <div class="col-2">
      </div>
      <div class="col-3">
          <div class="headerList">
              <ul>
                <li><p><i class='fa fa-facebook fa'></i> {fb}</p></li><li><p><i class='fa fa-twitter fa'></i>{tw}</p></li>
              </ul>
          </div>
      </div>
  </div>

<div class="row col-12 panel">
    <div class="col-6">
        {banner}
    </div>
    <div class="col-6">
        {date}
    </div>
</div>

<div class="row">
    <div class="col-3">
        <div class="slider datePanel">
            <ul>
                <!--  I know this is the complete wrong way, but I don't know the right way. Will finish it this way and fix it later. -->
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

                    $sql = "SELECT id, title, description, date FROM calendar";
                $result = mysqli_query($conn, $sql);

                if (mysqli_num_rows($result) > 0) {
                    // output data of each row
                    while($row = mysqli_fetch_assoc($result)) {
                        echo "<li><p class='calendarTextHead'>" . $row["title"] . "</p> <p class='calendarTextDate'>" . $row["date"] . "</p> <p class='calendarText'>" . $row["description"] . "</p>" . " ";
                    }
                } else {
                    echo "0 results";
                }

                mysqli_close($conn);
                ?>

            </ul>
        </div>
    </div>
    <div class="col-7">
        <div id="slider">
            <ul>
                <?php
                $dirname = "images/";
                $images = glob($dirname."*.*");

                foreach($images as $image) {
                echo "<li><img src='".$image."' /><br /></li>";
            }
                ?>
            </ul>
        </div>
    </div>
    <div class="col-2">
        <ul>
        <a class="twitter-timeline" href="{TWAPI}" data-chrome="noscrollbar" data-width="400" data-height="500" tweet-limit="3">
        </a>
    </ul>
    </div>
</div>


</body>
<script src="https://code.jquery.com/jquery-3.2.1.js" integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=" crossorigin="anonymous"></script>
<script>
    jQuery(document).ready(function($) {
        $('#checkbox').ready(function() {
            setInterval(function() {
                moveRight();
            }, 3000);
        });
        var slideCount = $('#slider ul li').length;
        var slideWidth = $('#slider ul li').width();
        var slideHeight = $('#slider ul li').height();
        var sliderUlWidth = slideCount * slideWidth;
        $('#slider').css({
            width: slideWidth,
            height: slideHeight
        });
        $('#slider ul').css({

        });
        $('#slider ul li:last-child').prependTo('#slider ul');
        function moveLeft() {
            $('#slider ul').animate({
                left: +slideWidth
            }, 200, function() {
                $('#slider ul li:last-child').prependTo('#slider ul');
                $('#slider ul').css('left', '');
            });
        };
        function moveRight() {
            $('#slider ul').animate({
                left: -slideWidth
            }, 200, function() {
                $('#slider ul li:first-child').appendTo('#slider ul');
                $('#slider ul').css('left', '');
            });
        };
        $('a.control_prev').click(function() {
            moveLeft();
        });
        $('a.control_next').click(function() {
            moveRight();
        });
    });
</script>
<script>
    var today = new Date();
    $('#date').html(today.toDateString());
</script>
<script>
    window.twttr = (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0],
            t = window.twttr || {};
        if (d.getElementById(id)) return t;
        js = d.createElement(s);
        js.id = id;
        js.src = "https://platform.twitter.com/widgets.js";
        fjs.parentNode.insertBefore(js, fjs);
        t._e = [];
        t.ready = function(f) {
            t._e.push(f);
        };
        return t;
    }(document, "script", "twitter-wjs"));
</script>


</html>
