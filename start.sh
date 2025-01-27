#!/bin/sh

# Initialize the Airflow database
airflow db init

# Create the admin user if it does not already exist
airflow users create \
    --username admin \
    --password admin \
    --firstname Anurag \
    --lastname S \
    --role Admin \
    --email anurag.techniknow@gmail.com

# Start the Airflow web server
airflow webserver -p 8080 &
# Start the Airflow scheduler
airflow scheduler
