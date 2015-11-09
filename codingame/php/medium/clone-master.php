<?php
    fscanf(STDIN, "%d %d %d %d %d %d %d %d",
        $nbFloors, // number of floors
        $width, // width of the area
        $nbRounds, // maximum number of rounds
        $exitFloor, // floor on which the exit is found
        $exitPos, // position of the exit on its floor
        $nbTotalClones, // number of generated clones
        $nbAdditionalElevators, // ignore (always zero)
        $nbElevators // number of elevators
    );

    $elevators = [];
    for ($i = 0; $i < $nbElevators; $i++) {
        fscanf(STDIN, "%d %d", $elevatorFloor, $elevatorPos);
        $elevators[$elevatorFloor] = $elevatorPos;
    }

    $blocks = [];
    while (true) {
        fscanf(STDIN, "%d %d %s", $cloneFloor, $clonePos, $direction);
        $directionPos = $exitPos;
        if ($cloneFloor != $exitFloor) {
            $directionPos = $elevators[$cloneFloor];
        }

        if (array_key_exists($cloneFloor, $blocks)) {
            echo "WAIT\n";
            continue;
        }

        if (($clonePos > $directionPos && $direction != 'LEFT')
            || ($clonePos < $directionPos && $direction != 'RIGHT')) {
            if (!array_key_exists($cloneFloor, $blocks)) {
                echo "BLOCK\n";
                $blocks[$cloneFloor] = true;
                continue;
            }
            $blocks[$cloneFloor] = 0;
        }

        echo "WAIT\n";
    }
