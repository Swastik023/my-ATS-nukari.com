from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests
import json

def fetch_candidate_data():
    # Fetch candidate data from an external API or service
    response = requests.get('https://api.example.com/candidates')
    candidates = response.json()
    # Save fetched data to a file or a database
    with open('/path/to/temp/candidates.json', 'w') as f:
        json.dump(candidates, f)

def process_candidate_data():
    # Load and process the data
    with open('/path/to/temp/candidates.json', 'r') as f:
        candidates = json.load(f)
    
    processed_candidates = []
    for candidate in candidates:
        processed_candidates.append({
            "name": candidate['name'],
            "email": candidate['email'],
            "skills": candidate.get('skills', []),
            # Other processing steps...
        })
    
    # Save processed data to another file
    with open('/path/to/temp/processed_candidates.json', 'w') as f:
        json.dump(processed_candidates, f)

def load_candidate_data():
    # Load the processed candidate data into your database
    with open('/path/to/temp/processed_candidates.json', 'r') as f:
        candidates = json.load(f)
    
    # Insert the data into your database
    from models import db, Candidate
    for candidate_data in candidates:
        candidate = Candidate(
            name=candidate_data['name'],
            email=candidate_data['email'],
            skills=candidate_data['skills'],
            experience=candidate_data.get('experience', []),
            education=candidate_data.get('education', [])
        )
        db.session.add(candidate)
    db.session.commit()

# Define the Airflow DAG
dag = DAG(
    'candidate_data_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily'  # Run daily
)

# Define tasks
fetch_task = PythonOperator(task_id='fetch_data', python_callable=fetch_candidate_data, dag=dag)
process_task = PythonOperator(task_id='process_data', python_callable=process_candidate_data, dag=dag)
load_task = PythonOperator(task_id='load_data', python_callable=load_candidate_data, dag=dag)

# Set task dependencies
fetch_task >> process_task >> load_task
