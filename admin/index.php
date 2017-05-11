<html>
<?php

    include 'header.php';

    ?>

    <body>

        <div class="row">
            <div class="col-3">
                <h3> Add new event</h3>
                <p>
                    Enter the details of the event you'd like to add to the calendar
                </p>
                <form action="insert.php" method="post">
                    <p>
                        Date:
                    </p>
                    <input type="text" name="date" required placeholder="YYYY-MM-DD">
                    <p>
                        Title:
                    </p>
                    <input type="text" name="title" required placeholder="Give your event a title">
                    <p>
                        Description:
                    </p>
                    <input type="text" name="description" required placeholder="Describe what's happening">
                    <input type="submit" value="Submit"><br>
                </form>
            </div>
            <div class="col-3">
                <h3>Remove event</h3>
                <p>
                    Enter the date of the event you would like to remove:
                </p>
                <form action="remove.php" method="post">
                    <p>
                        Date:
                    </p>
                    <input type="text" name="date" required placeholder="YYYY-MM-DD">
                    <input type="submit" value="Submit"><br>
                </form>
            </div>
        </div>
    </body>

</html>
