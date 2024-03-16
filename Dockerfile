# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install needed dependencies
RUN apt-get update && apt-get install -y \
    libmagic-dev \
    youtube-dl \
    ffmpeg

RUN pip install --no-cache-dir youtube-dl
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "main.py"]
