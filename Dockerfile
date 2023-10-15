FROM debian:11

RUN apt-get upgrade -y

RUN apt-get update -y

RUN apt-get install git vim gcc adduser python3-pip -y

RUN adduser --home /home/user --system user

WORKDIR /home/user

USER user

COPY ./requirements.txt /home/user/requirements.txt

RUN pip3 install -r requirements.txt --user

COPY --chown=user:nogroup ./source /home/user/

WORKDIR /home/user



