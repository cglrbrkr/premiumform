# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --trusted-host pypi.python.org Flask

# Make port 5999 available to the world outside this container
EXPOSE 5999

# Define an environment variable
# Set environment variable to ensure output
# is sent straight to the terminal
ENV PYTHONUNBUFFERED 1



# Run your application when the container launches
CMD ["python", "app.py"]

