<html>

<head>
    <title>Localhost - Thorium</title>
    <link rel="stylesheet" href="/css/style.css">
    <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
    <link rel="stylesheet" href="/css/grid.css" </head>

    <body>
        <!-- Header part -->
        <h1>Header</h1>
        <!-- Body Part -->
        <p>Libre ipsum something all work and no play makes homer something something</p>



        <div id="slideshow">
            <div>
                <img src="/images/1.jpg">
            </div>
            <div>
                <img src="/images/2.jpg">
            </div>
            <div>
                <img src="/images/3.jpg">
            </div>
        </div>

        <!-- Footer Part -->


    </body>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
    <script>
        $("#slideshow > div:gt(0)").hide();

        setInterval(function() {
            $('#slideshow > div:first')
                .fadeOut(1000)
                .next()
                .fadeIn(1000)
                .end()
                .appendTo('#slideshow');
        }, 3000);

    </script>

</html>
