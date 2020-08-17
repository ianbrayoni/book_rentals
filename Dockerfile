FROM python:3.7

# app files
COPY . /usr/src/app
WORKDIR /usr/src/app

# install packaging tool and install dependencies
RUN pip install pipenv
RUN pipenv install