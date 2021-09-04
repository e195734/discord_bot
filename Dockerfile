FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales libffi-dev libnacl-dev python3-dev chromium && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

ADD . /code
WORKDIR /code
RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN sed -i -e "s@pyppeteer.launch(@pyppeteer.launch(executablePath='/usr/bin/chromium', @" /usr/local/lib/python3.9/site-packages/requests_html.py
