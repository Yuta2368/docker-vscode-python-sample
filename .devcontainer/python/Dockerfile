FROM python:3.8.1
WORKDIR /app
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y vim apt-utils
