<?php
    while (true) {
        fscanf(STDIN, "%d %d", $spaceX, $spaceY);

        $mountains = [];
        for ($i = 0; $i < 8; $i++) {
            fscanf(STDIN, "%d", $mountainH);
            $mountains[] = $mountainH;
        }

        arsort($mountains, SORT_NUMERIC);

        echo ($spaceX == array_keys($mountains)[0]) ? "FIRE\n" : "HOLD\n";
    }
