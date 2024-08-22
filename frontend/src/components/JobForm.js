import React, { useState } from 'react';

function JobForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [requirements, setRequirements] = useState('');
  const [location, setLocation] = useState('Remote');
  const userId = 1;  // Hardcoded for now

  const handleSubmit = (event) => {
    event.preventDefault();
    const jobDetails = {
      title,
      description,
      requirements,
      location,
      posted_by: userId
    };

    fetch('/api/job_postings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(jobDetails)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Job posted successfully:', data);
    })
    .catch(error => {
      console.error('Error posting job:', error);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Job Title:</label>
        <input type="text" value={title} onChange={e => setTitle(e.target.value)} required />
      </div>
      <div>
        <label>Description:</label>
        <textarea value={description} onChange={e => setDescription(e.target.value)} required />
      </div>
      <div>
        <label>Requirements:</label>
        <input type="text" value={requirements} onChange={e => setRequirements(e.target.value)} />
      </div>
      <div>
        <label>Location:</label>
        <input type="text" value={location} onChange={e => setLocation(e.target.value)} />
      </div>
      <button type="submit">Post Job</button>
    </form>
  );
}

export default JobForm;
