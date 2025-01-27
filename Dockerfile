# Use a lightweight Python base image
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy only requirements first (for Docker layer caching)
COPY requirements.txt /app/

# Install system dependencies and Python dependencies in one step
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . /app/

# Set environment variables
ENV AWS_DEFAULT_REGION="eu-north-1"
ENV BUCKET_NAME="mynetsecurity"
ENV PREDICTION_BUCKET_NAME="my-network-datasource"
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True

# Add execution permissions to the start.sh script
RUN chmod +x /app/start.sh

# Expose any necessary ports (e.g., 8080 for web server)
EXPOSE 8080

# Set the entrypoint and command
ENTRYPOINT ["/bin/sh"]
CMD ["start.sh"]
