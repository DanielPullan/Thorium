<div class="row">
    <div class="col-3">
        <div class="slider datePanel">
            <ul>
                <<?php
                include (__DIR__.'/calendarData.php');
                ?>
            </ul>
        </div>
    </div>
    <div class="col-7">
        <div id="slider">
            <ul>
                <?php
                $xml = simplexml_load_file('slider.xml');

            // thanks madison for showing me how to make this bit work
                foreach($xml->children() as $image) {
                    echo "<li>
                            <img src='".$image->link."' />
                        </li>";
                }
                ?>
            </ul>
        </div>
    </div>
    <div class="col-2">
        <a class="twitter-timeline" href="https://twitter.com/poole_high" data-chrome="noscrollbar" data-width="400" data-height="500" tweet-limit="3">
        </a>
    </div>
</div>
