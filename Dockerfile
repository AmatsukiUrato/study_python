FROM ubuntu:18.04

MAINTAINER Admin <tomoaki.matsuura@ari-jp.com>

# install packages
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get autoremove -y
RUN apt-get install -y python3.7
RUN apt-get install -y git
RUN apt-get install -y tree