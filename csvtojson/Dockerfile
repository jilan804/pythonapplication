# pull official base image
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip==21.3
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .