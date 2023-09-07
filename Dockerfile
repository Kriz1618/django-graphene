FROM python:3.11-slim 

WORKDIR /app

RUN apt-get update

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
