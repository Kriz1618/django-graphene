FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Start with UWSGI
# CMD ["uwsgi", "--ini", "uwsgi.ini"]
