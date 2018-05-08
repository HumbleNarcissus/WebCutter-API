FROM python:3.6-slim
LABEL maintainer="Maciej Tarach"
LABEL contact="maciek.tarach06@gmail.com"

ENV INSTALL_PATH /webcutter
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .



CMD gunicorn -b 0.0.0.0:8000 run:app
