FROM python:3.7.9
LABEL maintainer mohinesh

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput
RUN python manage.py crontab add

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT