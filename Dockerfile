FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "run:app"]
