# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /code
WORKDIR /ecoseva

# Copy the requirements file into the container and install dependencies
COPY requirements/requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . .

# Expose the port that Django runs on
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]