FROM python:3.7.16-slim

WORKDIR /app
COPY ./app.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./templates ./templates
COPY ./events.csv .
ENV PYTHONUNBUFFERED=1

ENTRYPOINT  python3 app.py


