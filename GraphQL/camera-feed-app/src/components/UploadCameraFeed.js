import React, { useState } from 'react';
import { useMutation, gql } from '@apollo/client';

const UPLOAD_CAMERA_FEED_MUTATION = gql`
  mutation UploadCameraFeed($input: UploadCameraFeedInput!) {
    uploadCameraFeed(input: $input) {
      id
      customerId
      feedType
      encryptedData
      timestamp
      insights {
        id
        description
        timestamp
      }
    }
  }
`;

const UploadCameraFeed = () => {
  const [customerId, setCustomerId] = useState('');
  const [feedType, setFeedType] = useState('RGB');
  const [data, setData] = useState('');
  const [timestamp, setTimestamp] = useState('');
  const [uploadCameraFeed, { data: uploadData, error }] = useMutation(UPLOAD_CAMERA_FEED_MUTATION);

  const handleUpload = async (e) => {
    e.preventDefault();
    try {
      await uploadCameraFeed({
        variables: {
          input: {
            customerId,
            feedType,
            data,
            timestamp,
          },
        },
      });
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Upload Camera Feed</h2>
      <form onSubmit={handleUpload}>
        <div>
          <label>Customer ID</label>
          <input type="text" value={customerId} onChange={(e) => setCustomerId(e.target.value)} />
        </div>
        <div>
          <label>Feed Type</label>
          <select value={feedType} onChange={(e) => setFeedType(e.target.value)}>
            <option value="RGB">RGB</option>
            <option value="INFRARED">Infrared</option>
          </select>
        </div>
        <div>
          <label>Data (base64 encoded)</label>
          <input type="text" value={data} onChange={(e) => setData(e.target.value)} />
        </div>
        <div>
          <label>Timestamp</label>
          <input type="text" value={timestamp} onChange={(e) => setTimestamp(e.target.value)} />
        </div>
        <button type="submit">Upload</button>
      </form>
      {uploadData && <p>Upload successful!</p>}
      {error && <p>Error uploading feed</p>}
    </div>
  );
};

export default UploadCameraFeed;
