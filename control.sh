#!/bin/bash
function start {  
            echo "Starting containers"
            echo "............................"
            echo ".................................................................."
            docker-compose -f docker-compose.yml up &
            docker run -d --name ubuntu-docker ubuntu/testing5

}

function stop {  
            echo "Stoping containers"
            echo "............................"
            echo ".................................................................."
            docker-compose -f docker-compose.yml down &&
            #docker stop ubuntu-docker &
            docker rm --force ubuntu-docker

}

function clean_network {  
            echo "Pruning docker network"
            echo "............................"
            echo ".................................................................."
            docker network prune

}



if [ $1 = "start" ]; then
    start
fi

if [ $1 = "stop" ]; then
    stop
fi

if [ $1 = "clean_network" ];then
    clean_network
fi