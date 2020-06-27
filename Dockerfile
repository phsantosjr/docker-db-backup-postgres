FROM ubuntu

MAINTAINER Paulo Henrique <contato@lojaconectada.com.br>

WORKDIR /opt

RUN apt-get update && apt-get install -my wget gnupg

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update && apt-get install -y apt-utils apt-transport-https ca-certificates

RUN apt-get -y -q install software-properties-common
RUN apt-get -y -q install postgresql postgresql-contrib

RUN apt-get install python3-pip python-dev -y

RUN pip3 install --upgrade pip
RUN pip3 install python-dateutil python-magic requests
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


