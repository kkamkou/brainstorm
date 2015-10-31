<?php
    while (true) {
        fscanf(STDIN, "%s", $enemy1);
        fscanf(STDIN, "%d", $dist1);
        fscanf(STDIN, "%s", $enemy2);
        fscanf(STDIN, "%d", $dist2);

        $set = [$dist1 => $enemy1, $dist2 => $enemy2];
        echo $set[min($dist1, $dist2)] . "\n";
    }
