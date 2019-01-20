FROM ubuntu

RUN apt-get -yqq update
RUN apt-get -yqq install python3 python3-gnupg
RUN useradd hackathon

COPY src/ /home/hackathon
COPY configs/ /home/hackathon/configs
WORKDIR /home/hackathon
RUN python3 askkey.py

CMD [ "python3", "messager.py"]
