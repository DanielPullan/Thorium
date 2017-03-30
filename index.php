<html>

<head>
    <title>Localhost - Thoriums
    </title>
    <link rel="stylesheet" href="/css/style.css">
    <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
    <link rel="stylesheet" href="/css/simple-grid.css">
</head>

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<link href="/lib/jquery.bxslider.css" rel="stylesheet" />
<script src="/js/jquery.bxslider.min.js"></script>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</head>

<body>
    <!-- Header part -->
    <div class="row">
        <div class="col-2"></div>
        <div class="col-8">
            <h1>Poole High School</h1>
            <p>twitter.com/Poole_High facebook.com/poolehs</p>
        </div>
    </div>

    <!-- Body Part -->

    <div class="row">
        <div class="col-2">
            <ul class="bxslider2">
                <li>
                    <p>Something happened</p>
                </li>
                <li>
                    <p>Something else happened</p>
                </li>
                <li>
                    <p>yet more stuff happened</p>
                </li>
            </ul>
        </div>
        <div class="col-8">
            <ul class="bxslider">
                <li><img src="/images/1.jpg" />
                    <p>Something happened</p>
                </li>
                <li><img src="/images/2.jpg" />
                    <p>Something else happened</p>
                </li>
                <li><img src="/images/3.jpg" />
                    <p>yet more stuff happened</p>
                </li>
            </ul>
        </div>
        <div class="col-2">
            <a class="twitter-timeline" href="https://twitter.com/poole_high" theme="dark" data-chrome="noscrollbar transparent" data-width="400" data-height="800" tweet-limit="3">
</a>
        </div>
    </div>

    <!-- Footer Part -->


</body>

<script>
    $('.bxslider').bxSlider({
        auto: true,
        autoControls: true,
        speed: 800
    });

    $('.bxslider2').bxSlider({
        auto: true,
        autoControls: true,
        speed: 800
    });

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
