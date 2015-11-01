<?php
    fscanf(STDIN, "%d", $N);
    fscanf(STDIN, "%d", $Q);

    $list = [];
    for ($i = 0; $i < $N; $i++) {
        fscanf(STDIN, "%s %s", $ext, $mt);
        $list[strtolower($ext)] = $mt;
    }

    for ($i = 0; $i < $Q; $i++) {
        $ext = strtolower(pathinfo(stream_get_line(STDIN, 500, "\n"), PATHINFO_EXTENSION));
        echo (isset($list[$ext]) ? $list[$ext] : 'UNKNOWN') . "\n";
    }
