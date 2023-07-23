import axios from 'axios';

// Function to set the Authorization header with the provided token
export function setAuthorizationHeader(token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}
  
// Function to check if the user is authenticated
export function isAuthenticated() {
    const token = localStorage.getItem('token');
    return !!token;
}