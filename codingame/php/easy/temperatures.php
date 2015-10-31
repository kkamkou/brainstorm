<?php
    fscanf(STDIN, "%d", $n);

    $min = null;
    $list = explode(' ', $temps);
    $temps = stream_get_line(STDIN, 256, "\n");

    foreach ($list as $int) {
        if ($min === null || abs($min) > abs($int)  ) {
            $min = $int;
        }
    }

    echo in_array(abs($min), $list) ? abs($min) : $min;
