<?php
    fscanf(STDIN, "%d", $surfaceN);
    for ($i = 0; $i < $surfaceN; $i++) {
        fscanf(STDIN, "%d %d", $landX, $landY);
    }

    while (true) {
        fscanf(
            STDIN, "%d %d %d %d %d %d %d", $X, $Y, $hSpeed, $vSpeed, $fuel, $rotate, $power
        );

        $p =0;
        if ($vSpeed <= -40){
            $p = 4;
        }

        echo("0 $p\n");
    }
