from flask import Blueprint, request, jsonify
from models import db, JobPosting, Application
from naukri_api import post_job, search_resumes, match_candidates, get_applications

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/job_postings', methods=['POST'])
def add_job_posting():
    data = request.json
    job_posting = JobPosting(
        title=data['title'],
        description=data['description'],
        requirements=data.get('requirements', []),
        location=data.get('location', 'Remote'),
        posted_by=data['posted_by']
    )
    db.session.add(job_posting)
    db.session.commit()

    # Post the job on Naukri.com
    naukri_response = post_job({
        "title": data['title'],
        "description": data['description'],
        "location": data['location'],
        "requirements": data.get('requirements', []),
    })

    return jsonify({
        'message': 'Job posting added successfully',
        'job_id': job_posting.job_id,
        'naukri_response': naukri_response
    })

@api_blueprint.route('/resumes/search', methods=['POST'])
def search_resumes_route():
    search_criteria = request.json
    resumes = search_resumes(search_criteria)
    return jsonify(resumes)

@api_blueprint.route('/jobs/<int:job_id>/match_candidates', methods=['GET'])
def match_candidates_route(job_id):
    matched_candidates = match_candidates(job_id)
    return jsonify(matched_candidates)

@api_blueprint.route('/jobs/<int:job_id>/applications', methods=['GET'])
def get_job_applications(job_id):
    applications = get_applications(job_id)
    return jsonify(applications)
