import React from 'react';
import './styles.css';

const Results = ({ data }) => {
  if (!data) return null;

  const { 
    summary = 'No summary available.',
    fit_score = 0,
    missing_keywords = [],
    strengths = [],
    weaknesses = [],
    improvement_suggestions = [],
    ai_suggestions = ''
  } = data;

  const getScoreColor = (score) => {
    if (score >= 80) return '#4CAF50'; // Green
    if (score >= 60) return '#FFC107'; // Yellow
    return '#F44336'; // Red
  };

  return (
    <div className="results-container">
      <div className="score-header">
        <h2>Analysis Results</h2>
        <div 
          className="score-circle"
          style={{ 
            backgroundColor: getScoreColor(fit_score),
            borderColor: getScoreColor(fit_score)
          }}
        >
          {fit_score}
        </div>
      </div>

      <div className="result-section">
        <h3>Summary</h3>
        <p>{summary}</p>
      </div>

      <div className="grid-container">
        <div className="result-section strengths">
          <h3>Strengths</h3>
          {strengths.length > 0 ? (
            <ul>
              {strengths.map((item, index) => (
                <li key={index}>✅ {item}</li>
              ))}
            </ul>
          ) : <p>No strengths identified.</p>}
        </div>

        <div className="result-section weaknesses">
          <h3>Weaknesses</h3>
          {weaknesses.length > 0 ? (
            <ul>
              {weaknesses.map((item, index) => (
                <li key={index}>⚠️ {item}</li>
              ))}
            </ul>
          ) : <p>No weaknesses found.</p>}
        </div>
      </div>

      {missing_keywords.length > 0 && (
        <div className="result-section">
          <h3>Missing Keywords</h3>
          <div className="keywords-container">
            {missing_keywords.map((keyword, index) => (
              <span key={index} className="keyword-pill">{keyword}</span>
            ))}
          </div>
        </div>
      )}

      {improvement_suggestions.length > 0 && (
        <div className="result-section">
          <h3>Improvement Suggestions</h3>
          <ul className="suggestions-list">
            {improvement_suggestions.map((suggestion, index) => (
              <li key={index}>✨ {suggestion}</li>
            ))}
          </ul>
        </div>
      )}

      {ai_suggestions && (
        <div className="result-section ai-suggestions">
          <h3>AI Recommendations</h3>
          <p>{ai_suggestions}</p>
        </div>
      )}
    </div>
  );
};

export default Results;
