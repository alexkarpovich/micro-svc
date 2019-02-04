FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src

RUN pip install pipenv
COPY ./ui-mcs/Pipfile ./ui-mcs/Pipfile.lock /usr/src/
RUN pipenv install --system

COPY ./ui-mcs /usr/src/

# RUN python -m grpc_tools.protoc -I/protos --python_out=./proto --grpc_python_out=./proto /protos/snip.proto
