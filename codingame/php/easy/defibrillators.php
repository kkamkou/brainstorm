<?php
    fscanf(STDIN, "%s", $LON);
    fscanf(STDIN, "%s", $LAT);
    fscanf(STDIN, "%d", $N);

    function php_type_fix(&$val) {
        $val = str_replace(',', '.', $val);
    }

    php_type_fix($LON);
    php_type_fix($LAT);

    $min = $title = null;
    for ($i = 0; $i < $N; $i++) {
        $defib = explode(';', stream_get_line(STDIN, 256, "\n"));

        php_type_fix($defib[4]);
        php_type_fix($defib[5]);

        $x = ($defib[4] - $LON) * cos(($LAT + $defib[5]) / 2);
        $y = $defib[5] - $LAT;

        $res = sqrt(pow($x, 2) + pow($y, 2)) * 6371;
        if ($min === null || $min > $res) {
            $min = $res;
            $title = $defib[1];
        }
    }

    echo($title . "\n");
