<?php
    fscanf(STDIN, "%d", $road);
    fscanf(STDIN, "%d", $gap);
    fscanf(STDIN, "%d", $platform);

    while (true) {
        fscanf(STDIN, "%d", $speed);
        fscanf(STDIN, "%d", $coordX);

        $speedRequired = $gap + 1;

        if ($coordX >= $road + $gap) {
            echo("SLOW\n");
            continue;
        }

        if ($speed != $speedRequired) {
            echo($speed < $speedRequired ? "SPEED\n" : "SLOW\n");
            continue;
        }

        if ($coordX + 1 == $road) {
            echo("JUMP\n");
            continue;
        }

        echo "WAIT\n";
    }
