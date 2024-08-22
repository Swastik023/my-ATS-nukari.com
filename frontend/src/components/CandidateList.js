import React, { useState, useEffect } from 'react';
import CandidateProfile from './CandidateProfile';

function CandidateList() {
  const [candidates, setCandidates] = useState([]);
  const [selectedCandidate, setSelectedCandidate] = useState(null);

  useEffect(() => {
    fetch('/api/candidates')
      .then(response => response.json())
      .then(data => setCandidates(data));
  }, []);

  const handleSelectCandidate = (candidate) => {
    setSelectedCandidate(candidate);
  };

  return (
    <div>
      <h2>Candidates</h2>
      <ul>
        {candidates.map(candidate => (
          <li key={candidate.candidate_id} onClick={() => handleSelectCandidate(candidate)}>
            {candidate.name}
          </li>
        ))}
      </ul>
      {selectedCandidate && <CandidateProfile candidate={selectedCandidate} />}
    </div>
  );
}

export default CandidateList;
