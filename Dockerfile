FROM ubuntu:22.04

MAINTAINER Paulo Henrique <ph@phgr.tech>

WORKDIR /opt

RUN apt-get update && apt-get install -my wget gnupg
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN apt-get update && apt-get install -y apt-utils apt-transport-https ca-certificates
RUN apt-get install -y -q -f software-properties-common #postgresql postgresql-contrib
RUN apt-get install postgresql-client-14 python3-pip -y

RUN pip install --upgrade pip
RUN pip install python-dateutil python-magic requests
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt


