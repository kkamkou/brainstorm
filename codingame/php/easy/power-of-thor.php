<?php
    // west, east, north, south

    fscanf(STDIN, "%d %d %d %d", $lightX, $lightY, $initialTX, $initialTY);

    $thorX = $initialTX;
    $thorY = $initialTY;

    function direction(&$coord, $needed, $opts, $max)
    {
        if ($coord == $needed) {
            return '';
        }

        if ($coord > $needed) {
            $dir = $opts[0];
            $coord--;
        } else {
            $dir = $opts[1];
            $coord++;
        }

        if ($coord < 1) {
            $dir = $opts[0];
        }

        return $dir;
    }

    while (true) {
        fscanf(STDIN, "%d", $remainingTurns);

        $directionX = direction($thorX, $lightX, ['W', 'E'], 38);
        $directionY = direction($thorY, $lightY, ['N', 'S'], 17);

        echo $directionY . $directionX . "\n";
    }
