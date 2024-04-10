FROM python:3-alpine

RUN pip install poetry 

RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY . .

RUN poetry install

