import React, { useState, useEffect } from 'react';

function JobList() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    fetch('/api/job_postings')
      .then(response => response.json())
      .then(data => setJobs(data));
  }, []);

  return (
    <div>
      <h2>Job Openings</h2>
      <ul className="list-group">
        {jobs.map(job => (
          <li key={job.job_id} className="list-group-item">
            <h4>{job.title}</h4>
            <p>{job.location}</p>
            <p>{job.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default JobList;
