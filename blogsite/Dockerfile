# Use an official Python runtime as a parent image
FROM python:3.6
#LABEL maintainer="greg@wagfront.com"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# set work directory
WORKDIR /usr/src/blogsite

# use config.settings.dev so we can serve media files without using AWS s3
ENV PYTHONPATH=/usr/src/blogsite \
	DJANGO_SETTINGS_MODULE=blogsite.settings.dev \
	PORT=8000 \
	WEB_CONCURRENCY=3 \
	GUNICORN_CMD_ARGS="--max-requests 1200 --access-logfile -"

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/blogsite/Pipfile

# Install any needed packages specified in requirements.txt
RUN pipenv install --skip-lock --system --dev
#RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /usr/src/blogsite/
# Set the working directory to /code/
# WORKDIR /code/

#RUN python manage.py migrate

#RUN useradd wagtail
#RUN chown -R wagtail /code
#USER wagtail

#EXPOSE 8000
#CMD exec gunicorn #blogsite.wsgi:application --bind 0.0.0.0:8000 --workers 3
