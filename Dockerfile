FROM python:3.8

RUN pip install pipenv
COPY Pipfile* /app/
WORKDIR /app
RUN pipenv install
COPY . /app/

CMD ["pipenv", "run", "uvicorn", "--host", "0.0.0.0", "--port", "$PORT", "--loop", "uvloop", "app.main:app"]
