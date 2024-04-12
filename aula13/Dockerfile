FROM python:3.12

RUN pip3 install poetry 

RUN poetry config virtualenvs.create false

WORKDIR /app

VOLUME ["/app"]

COPY . .

RUN poetry install

EXPOSE 8000

CMD python -m api.run 