import axios from 'axios';

export const getMembers = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/members/');
    return response.data;
  } catch (error) {
    console.error("There was an error fetching the members!", error);
  }
}
