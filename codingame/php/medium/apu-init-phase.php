<?php
    fscanf(STDIN, "%d", $width);
    fscanf(STDIN, "%d", $height);

    $lines = [];
    for ($i = 0; $i < $height; $i++) {
        $lines[] = str_split(stream_get_line(STDIN, 31, "\n"));
    }

    for ($h = 0; $h < $height; $h++) {
        for ($w = 0; $w < $width; $w++) {
            if ($lines[$h][$w] == '.') {
                continue;
            }

            $r = $w + 1;
            $b = $h + 1;

            $out = ["$w $h"];

            while ($width > $r && $lines[$h][$r] == '.') {
                $r++;
            }

            while ($height > $b && $lines[$b][$w] == '.') {
                $b++;
            }

            $out[] = ($width > $r && $lines[$h][$r] == '0') ? "$r $h" : '-1 -1';
            $out[] = ($height > $b && $lines[$b][$w] == '0') ? "$w $b" : '-1 -1';

            echo implode(' ', $out) . "\n";
        }
    }
