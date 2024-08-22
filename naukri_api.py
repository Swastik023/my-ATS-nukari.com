import requests
from config import Config

NAUKRI_BASE_URL = "https://api.naukri.com/v2"

headers = {
    "Authorization": f"Bearer {Config.NAUKRI_API_KEY}",
    "Content-Type": "application/json"
}

def post_job(job_details):
    url = f"{NAUKRI_BASE_URL}/jobs/post"
    response = requests.post(url, headers=headers, json=job_details)
    return response.json()

def search_resumes(search_criteria):
    url = f"{NAUKRI_BASE_URL}/resumes/search"
    response = requests.post(url, headers=headers, json=search_criteria)
    return response.json()

def match_candidates(job_id):
    url = f"{NAUKRI_BASE_URL}/jobs/{job_id}/match"
    response = requests.get(url, headers=headers)
    return response.json()

def get_applications(job_id):
    url = f"{NAUKRI_BASE_URL}/jobs/{job_id}/applications"
    response = requests.get(url, headers=headers)
    return response.json()
