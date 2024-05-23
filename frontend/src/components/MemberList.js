import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MemberList = () => {
  const [members, setMembers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/members/')
      .then(response => {
        setMembers(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching members:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h1>Member List</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {members.map(member => (
            <li key={member.id}>{member.username}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default MemberList;
