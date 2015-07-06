#Get the latest armv7 base image from
#https://registry.hub.docker.com/u/resin/armv7hf-debian/
FROM resin/armv7hf-debian:latest

MAINTAINER Shaun Mulligan <shaun@resin.io>

#Install python2 and pip
RUN apt-get update && apt-get install -y --no-install-recommends \
		python \
		python-dev \
		python-dbus \
		python-pip \
	&& rm -rf /var/lib/apt/lists/*

#install python packages with pip
RUN pip install flask

#copy our python source into /app in the container
COPY src/ /app

#run main.py when the container starts
CMD ["python","/app/main.py"]
