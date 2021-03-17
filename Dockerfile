FROM python:3
MAINTAINER akshit "akshitdevpura@gmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
#EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]