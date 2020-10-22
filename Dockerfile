FROM python:3.8

RUN pip install pipenv
COPY Pipfile* /app/
WORKDIR /app
RUN pipenv install
COPY . /app/

CMD ["pipenv", "run", "python", "-m", "app.main", "app/main.py"]
