<html>
    <?php

    include 'header.php';

    ?>

<body>

    <div class="row">
        <div class="col-3">
            <h3> Make an Announcement</h3>
            <p>
                Enter the details of the announcement you would like to make
            </p>
            <form action="insertAnnouncement.php" method="post">
                <p>
                    Icon
                </p>
                <small>
                    Label uses Font Awesome icons, you can see the selection <a href="http://fontawesome.io/cheatsheet/">here.</a>
                </small>
                <input type="text" name="icon" required placeholder="fa fa-steam fa">
                <p>
                    Announcement
                </p>
                <input type="text" name="notice" required placeholder="Steam sale in three days">
                <input type="submit" value="Submit"><br>
            </form>
        </div>

        <div class="col-3">
            <h3>Remove Announcement</h3>
            <p>
                Enter "remove" then click submit to remove the current announcement
            </p>
            <form action="removeAnnouncement.php" method="post">
                <input type="text" name="title" required placeholder="There is no undo button">
                <input type="submit" value="Submit"><br>
            </form>
        </div>
    </div>
</body>

</html>
