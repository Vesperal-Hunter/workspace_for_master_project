#!/bin/bash
# Start up everything needed to run the tester

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


function trykill() {
    test ! -z "${1}" && kill "${1}" &>/dev/null && wait "${1}"
}

NUM_EXPERIMENTS=300

function cleanup() {
    trykill "${MORSE}"
    trykill "${POSEINIT}"
    trykill "${TEST}"
    trykill "${MONGODB}"

    wait
    exit
}

trap cleanup SIGINT SIGKILL SIGTERM

i=0
while (( $i < $NUM_EXPERIMENTS )); do

    roslaunch mongodb_store mongodb_store.launch db_path:=/home/hanshuyu/data2  &
    MONGODB="${!}"
    echo "Starting Openni. Please wait ..."
    sleep 5

         &
    MORSE="${!}"
    echo "Starting MORSE. Please wait ..."
    sleep 10


    rosrun pose_initialiser n.py &
    POSEINIT="${!}"
    sleep 3
    wait "${POSEINIT}"
    echo "set initial pose. Please wait ..."

    timeout 240s rosrun topological_navigation nav_client.py End 
    TEST="${!}"
    echo "TESTING. Please wait ..."
    echo "TESTING DONE"
    wait 60
    
    trykill "${TEST}"
    TEST=''
 
    trykill "${MONGODB}"
    MONGODB=''
  
    trykill "${MORSE}"
    MORSE=''

    wait

    i=$(( $i + 1 ))
done

cleanup
