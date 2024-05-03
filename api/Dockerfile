# Use the official Python image as a base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /api

# Copy the current directory contents into the container at /app
COPY . /api

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
