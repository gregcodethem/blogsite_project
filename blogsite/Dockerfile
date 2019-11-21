# Use an official Python runtime as a parent image

FROM python:3.7
#LABEL maintainer="hello@wagtail.io"


# Added from tutorial
WORKDIR /usr/src/blogsite

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /blogsite/requirements.txt

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/blogsite/Pipfile

# Install any needed packages specified in requirements.txt
RUN pip install -r /blogsite/requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
# Edited to follow tutorial
COPY . /usr/src/blogsite/
# Set the working directory to /code/
#WORKDIR /usr/src/blogsite/


#RUN python manage.py migrate

#RUN useradd wagtail

#RUN chown -R wagtail /usr/src/blogsite
#USER wagtail

#EXPOSE 8000
#CMD exec gunicorn blogsite.wsgi:application --bind 0.0.0.0:8000 --workers 3
