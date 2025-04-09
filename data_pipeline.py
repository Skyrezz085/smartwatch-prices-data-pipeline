'''
This program automates the ETL (Extract, Transform, Load) process using Apache Airflow.

Workflow:
1. Extract data from a PostgreSQL database.
2. Clean the data (remove duplicates, normalize column names, fill missing values).
3. Load the cleaned data into an Elasticsearch index for further analysis and search capabilities.

Each step is represented as a PythonOperator in the Airflow DAG.
'''

# Import required libraries
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2
from elasticsearch import Elasticsearch
import os

def fetch_from_postgresql(**kwargs):
    '''
    This function is used to fetch data from PostgreSQL and save it as a CSV file.

    The function connects to a PostgreSQL database using a predefined connection string, 
    executes a query to fetch data from a specific table, and then saves the result in CSV format 
    to a specified location.

    No parameters are required as the connection string and query are already defined within the function.

    Return:
        None - This function does not return any value; it performs the data fetching and saving process.

    Example usage:
        In an Airflow DAG, this function is called as part of the workflow:
        fetch_data = PythonOperator(
            task_id='fetch_from_postgresql', 
            python_callable=fetch_from_postgresql
        )

    Notes:
        This function fetches data from the `table_m3` table in the PostgreSQL database and saves it 
        as a CSV file named 'raw_data.csv' in the Airflow container.
    '''
    try:
        conn = psycopg2.connect(
            host="host.docker.internal",
            port=5432,
            database="postgres",
            user="postgres",
            password="postgres"
        )

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM public.table_m3;")
            df = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])

        conn.close()
        df.to_csv('raw_data.csv', index=False)

    except Exception as e:
        print(f"Error fetching data from PostgreSQL: {e}")
        raise

def data_cleaning(**kwargs):
    '''
    This function is used to clean raw data and save the cleaned version as a new CSV file.

    It performs three main operations:
    1. Removes duplicate rows from the dataset.
    2. Normalizes column names (lowercase, underscores, removes special characters).
    3. Fills missing/null values with a default placeholder ('N/A').

    Input:
        Reads the file 'raw_data.csv' from the current working directory.

    Return:
        None - This function does not return any value; it writes the cleaned data to 'clean_data.csv'.

    Example usage:
        clean_data = PythonOperator(
            task_id='data_cleaning',
            python_callable=data_cleaning
        )

    Notes:
        The cleaned data is saved as 'clean_data.csv' and used in the next stage of the ETL process.
    '''
    try:
        df = pd.read_csv('raw_data.csv')
        df = df.drop_duplicates()
        df.columns = [col.strip().lower().replace(" ", "_").replace("|", "") for col in df.columns]
        df = df.fillna('N/A')
        df.to_csv('clean_data.csv', index=False)

    except Exception as e:
        print(f"Error cleaning data: {e}")
        raise

def post_to_elasticsearch(**kwargs):
    '''
    This function is used to load cleaned data into an Elasticsearch index.

    It reads a cleaned CSV file and posts each row as an individual JSON document to the 
    specified Elasticsearch index.

    Input:
        Reads the file 'clean_data.csv' from the current working directory.

    Return:
        None - This function does not return any value; it sends data directly to Elasticsearch.

    Example usage:
        post_data = PythonOperator(
            task_id='post_to_elasticsearch',
            python_callable=post_to_elasticsearch
        )

    Notes:
        The data is indexed under 'smartwatch_data' in the running Elasticsearch instance.
    '''
    try:
        es = Elasticsearch(hosts=["http://elasticsearch:9200"])
        df = pd.read_csv('clean_data.csv')
        for index, row in df.iterrows():
            doc = row.to_dict()
            es.index(index="smartwatch_data", id=index, document=doc)

    except Exception as e:
        print(f"Error posting data to Elasticsearch: {e}")
        raise

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

# Define the DAG
with DAG(
    'P2M3_reza_DAG',
    default_args=default_args,
    description='Automation of Fetching, Cleaning, and Posting Data',
    schedule_interval='*/10 * * * *',
    start_date=datetime(2025, 1, 12),
    catchup=False,
    max_active_runs=1,
) as dag:

    # Task: Extract data from PostgreSQL
    fetch_task = PythonOperator(
        task_id='fetch_from_postgresql',
        python_callable=fetch_from_postgresql,
    )

    # Task: Transform data (cleaning)
    clean_task = PythonOperator(
        task_id='data_cleaning',
        python_callable=data_cleaning,
    )

    # Task: Load data into Elasticsearch
    post_task = PythonOperator(
        task_id='post_to_elasticsearch',
        python_callable=post_to_elasticsearch,
    )

    # Define the task pipeline
    fetch_task >> clean_task >> post_task