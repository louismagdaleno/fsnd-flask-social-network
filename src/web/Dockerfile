# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /web

# Copy the current directory contents into the container at /app
COPY . /web

# Install project requirements
RUN apt-get update && apt-get install -y \
        python-dev python-pip python-setuptools \
        libffi-dev libxml2-dev libxslt1-dev \
        libtiff5-dev libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev \
        liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
RUN pip install beautifulsoup4
# Add the dependencies to the container and install the python dependencies
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
RUN pip install Pillow

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME SocialNetwork



ENTRYPOINT [ "python" ]
CMD [ "manage.py" ]


#docker build . -t web
#docker run -t -i -p 8000:8000 web