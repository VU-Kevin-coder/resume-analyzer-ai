import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import Results from './components/Results';
import './styles.css';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (formData) => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData
      });
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Resume Analyzer AI</h1>
      <FileUpload onSubmit={handleSubmit} loading={loading} />
      {results && <Results data={results} />}
    </div>
  );
}

export default App;