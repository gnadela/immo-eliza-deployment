# Use the official Python image as a base image
FROM python:3.9-slim
# FROM python:3.11-slim-bookworm

# Set the working directory inside the container
WORKDIR /api

# Copy the requirements file into the container at /api
COPY requirements.txt /api/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the container at /api
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
