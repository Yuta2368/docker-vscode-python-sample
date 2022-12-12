FROM python:3.8.1
WORKDIR /app
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt
RUN apt-get -qq update \
&& apt-get -qq install -y vim apt-utils \
&& echo "alias ls='ls -lha --color=auto'" >> ~/.bashrc
