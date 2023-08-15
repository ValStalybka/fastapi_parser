FROM python:3.10-bullseye

ENV PYTHONUNBUFFERED=1

RUN pip install pipenv==2020.6.2

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy

COPY ./ .

RUN chmod +x ./*

ENTRYPOINT ["python3","main.py"]