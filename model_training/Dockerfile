# Dockerfile for LLM model service

# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app


RUN pip install --no-cache-dir transformers torch flask

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8001
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
