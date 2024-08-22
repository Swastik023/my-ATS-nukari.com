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
      <ul>
        {jobs.map(job => (
          <li key={job.job_id}>{job.title} - {job.location}</li>
        ))}
      </ul>
    </div>
  );
}

export default JobList;
