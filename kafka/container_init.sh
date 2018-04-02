#!/bin/sh

set ZOO_PID
set KFK_PID

function start_kafka(){

    /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties &
    ZOO_PID=$!

    sleep 5

    /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties &
    KFK_PID=$!
}

function stop_kafka(){
    kill $KFK_PID
    sleep 5
    kill $ZOO_PID
}

trap stop_kafka SIGTERM SIGINT
start_kafka
wait

