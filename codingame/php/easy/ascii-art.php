<?php

  fscanf(STDIN, "%d", $L);
  fscanf(STDIN, "%d", $H);

  $T = strtoupper(stream_get_line(STDIN, 256, "\n"));
  $set = range('A', 'Z');
  $set[] = '?';

  for ($i = 0; $i < $H; $i++) {
      $out = '';
      $line = stream_get_line(STDIN, 1024, "\n");

      foreach (str_split($T) as $char) {
          if (!in_array($char, $set)) {
              $char = '?';
          }
          $out .= substr($line, array_search($char, $set) * $L, $L);
      }

      echo  $out . "\n";
  }
