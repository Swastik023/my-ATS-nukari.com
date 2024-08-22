import React from 'react';
import Navbar from './components/Navbar';
import JobList from './components/JobList';
import CandidateProfile from './components/CandidateProfile';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="container">
        <JobList />
        <CandidateProfile />
      </div>
    </div>
  );
}

export default App;
