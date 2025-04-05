import React from 'react';
import { useNavigate } from 'react-router-dom';

function Dashboard({ setIsAuthenticated }) {
    const navigate = useNavigate();

    const handleLogout = async () => {
        const refreshToken = localStorage.getItem('refresh_token');
        const response = await fetch('http://127.0.0.1:8000/api/logout/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ refresh_token: refreshToken }),
        });
        if (response.ok) {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            setIsAuthenticated(false);
            navigate('/');
        } else {
            alert('Logout failed');
        }
    };

    return (
        <div>
            <h2>Dashboard</h2>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Dashboard;