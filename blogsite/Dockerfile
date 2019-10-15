# Use an official Python runtime as a parent image
FROM python:3.7.4-buster
#LABEL maintainer="greg@wagfront.com"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# set work directory
WORKDIR /usr/src/blogsite

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/blogsite/Pipfile

# Install any needed packages specified in requirements.txt
RUN pipenv install --skip-lock --system --dev
#RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /usr/src/blogsite/
# Set the working directory to /code/
WORKDIR /code/

#RUN python manage.py migrate

#RUN useradd wagtail
#RUN chown -R wagtail /code
#USER wagtail

#EXPOSE 8000
#CMD exec gunicorn #blogsite.wsgi:application --bind 0.0.0.0:8000 --workers 3
