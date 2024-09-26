#!/usr/bin/env bash

# Activate the Python virtual environment
source /opt/airflow/venv/bin/activate

# Initialize the Airflow database
airflow db reset --yes  # Use --yes to skip confirmation
airflow db init
airflow db upgradedb

# Create the Admin user
airflow users create \
    -r Admin \
    -u airflow \
    -e sameremadharb213@gmail.com \
    -f airflow \
    -l airflow \
    -p test1234

# Start the Airflow scheduler and webserver
airflow scheduler &

# Start the webserver in the foreground
exec airflow webserver
