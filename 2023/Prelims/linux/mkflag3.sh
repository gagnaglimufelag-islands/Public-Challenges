#!/bin/bash

root_dir=flag3

# Create 100 directories with random names
for i in {1..100}; do
    dir_name=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9/' | fold -w 20 | head -n 1)
    mkdir -p "$root_dir/$dir_name"
done

# Get a list of all the directories created
directories=$(find flag3 -type d)

# Add 300 files to a random selection of the directories
for i in {1..300}; do
    # Choose a random directory
    chosen_dir=$(echo $directories | tr ' ' '\n' | shuf -n 1)

    # Create a file with a random name and a unique and humorous string
    file_name=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
    unique_string=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 5 | head -n 1)
    leet_left="I_H4X0R3D_TH3"
    leet_right="M4TR1X_AND_4LL_1_G0T_W45_TH15_L0U5Y_5TR1NG"
    if [ $i -eq 100 ]
    then
        echo "gg{${leet_left}_31G3n_${leet_right}}" > "$chosen_dir/$file_name"
    else
        echo "g‎‎g{${leet_left}_${unique_string}_${leet_right}}" > "$chosen_dir/$file_name"
    fi
done

echo "Done!"
