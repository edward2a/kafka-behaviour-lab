FROM alpine:3.7

RUN apk update && \
    apk add openjdk8-jre-base bash pcre-tools

RUN addgroup -S kafka && \
    adduser -S -D -G kafka kafka

RUN wget http://ftp.heanet.ie/mirrors/www.apache.org/dist/kafka/1.1.0/kafka_2.11-1.1.0.tgz && \
    mkdir /opt && \
    tar -xf kafka_2.11-1.1.0.tgz -C /opt && \
    ln -s /opt/kafka_2.11-1.1.0 /opt/kafka

ADD config/zookeeper.properties /opt/kafka/config/zookeeper.properties
ADD config/server.properties /opt/kafka/config/server.properties
ADD container_init.sh /opt/kafka/bin/kafka-init.sh

RUN chmod 755 /opt/kafka/bin/kafka-init.sh

ENTRYPOINT /opt/kafka/bin/kafka-init.sh

ENV NET_IF=eth0 NET_PORT=9092
EXPOSE 9092
