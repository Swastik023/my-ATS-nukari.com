import React, { useState } from 'react';

function ResumeSearch() {
  const [skills, setSkills] = useState('');
  const [experience, setExperience] = useState('');

  const handleSearch = (event) => {
    event.preventDefault();
    const searchCriteria = {
      skills,
      experience
    };

    fetch('/api/resumes/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(searchCriteria)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Resumes found:', data);
    })
    .catch(error => {
      console.error('Error searching resumes:', error);
    });
  };

  return (
    <form onSubmit={handleSearch}>
      <div>
        <label>Skills:</label>
        <input type="text" value={skills} onChange={e => setSkills(e.target.value)} required />
      </div>
      <div>
        <label>Experience (years):</label>
        <input type="number" value={experience} onChange={e => setExperience(e.target.value)} required />
      </div>
      <button type="submit">Search Resumes</button>
    </form>
  );
}

export default ResumeSearch;
