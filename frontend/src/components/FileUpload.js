import React, { useRef, useState } from 'react';

function FileUpload({ onSubmit, loading }) {
  const [jobDescription, setJobDescription] = useState('');
  const [fileName, setFileName] = useState('No file chosen');
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFileName(file.name);
    } else {
      setFileName('No file chosen');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const file = fileInputRef.current?.files?.[0];
    if (!file) {
      alert('Please select a resume file.');
      return;
    }

    const formData = new FormData();
    formData.append('resume', file);
    formData.append('job_description', jobDescription.trim());

    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="upload-form" noValidate>
      {/* Resume Upload */}
      <div className="form-group file-upload-group">
        <label className="file-upload-label">
          Resume <span style={{ color: 'red' }}>*</span>
          <div className="file-upload-wrapper">
            <input
              type="file"
              accept=".pdf,.doc,.docx"
              ref={fileInputRef}
              onChange={handleFileChange}
              className="file-input"
              required
            />
            <div className="file-upload-button">Choose File</div>
            <span className="file-name">{fileName}</span>
          </div>
        </label>
      </div>

      {/* Job Description Textarea */}
      <div className="form-group">
        <label htmlFor="jd-textarea">Job Description (Optional):</label>
        <textarea
          id="jd-textarea"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          placeholder="Paste job description here..."
          className="jd-textarea"
        />
      </div>

      {/* Submit Button */}
      <button
        type="submit"
        disabled={loading}
        className="analyze-button"
        aria-busy={loading}
      >
        {loading ? (
          <>
            <span className="spinner" aria-hidden="true"></span> Analyzing...
          </>
        ) : (
          'Analyze Resume'
        )}
      </button>
    </form>
  );
}

export default FileUpload;
