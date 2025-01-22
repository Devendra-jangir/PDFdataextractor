import React, { useState } from 'react';
import axios from 'axios';

function PdfUploader() {
  const [file, setFile] = useState(null);
  const [details, setDetails] = useState({
    name: '',
    phone_number: '',
    address: '',
    role: ''
  });

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    if (!file) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    axios.post('http://localhost:5000/extract', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then((response) => {
      setDetails(response.data);
    })
    .catch((error) => {
      console.error('Error uploading file:', error);
    });
  };

  return (
    <div style={{ maxWidth: '500px', margin: 'auto', padding: '20px', textAlign: 'center', border: '1px solid #ddd', borderRadius: '10px' }}>
      <h2>Upload Resume</h2>
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <button onClick={handleUpload} style={{ marginLeft: '10px', padding: '8px 15px', cursor: 'pointer' }}>Upload</button>
      {details.name && (
        <div style={{ marginTop: '20px', textAlign: 'left' }}>
          <h3>Extracted Details:</h3>
          <p><strong>Name:</strong> {details.name}</p>
          <p><strong>Phone Number:</strong> {details.phone_number}</p>
          <p><strong>Address:</strong> {details.address}</p>
          <p><strong>Role:</strong> {details.role}</p>
        </div>
      )}
    </div>
  );
}

export default PdfUploader;
