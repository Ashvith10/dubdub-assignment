FROM python:3.10-slim-buster

WORKDIR /home

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --deploy

COPY . ./

EXPOSE 5000
