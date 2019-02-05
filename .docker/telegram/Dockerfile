FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src

RUN pip install pipenv
COPY ./telegram-mcs/Pipfile ./telegram-mcs/Pipfile.lock /usr/src/
RUN pipenv install --system

COPY ./telegram-mcs /usr/src/

# RUN python -m grpc_tools.protoc -I/protos --python_out=./proto --grpc_python_out=./proto /protos/snip.proto
