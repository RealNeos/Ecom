import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Register() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [firstName, setFirstName] = useState(''); // Added state for first name
    const [lastName, setLastName] = useState(''); // Added state for last name
    const navigate = useNavigate();

    const handleRegister = async (e) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:8000/api/signup/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username,
                email,
                password,
                first_name: firstName, // Include first name
                last_name: lastName, // Include last name
            }),
        });
        const data = await response.json();
        if (response.ok) {
            alert('Registration successful');
            navigate('/');
        } else {
            alert(data.error || 'Registration failed');
        }
    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleRegister}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="First name"
                    value={firstName} // Updated to use correct state
                    onChange={(e) => setFirstName(e.target.value)} // Updated handler
                />
                <input
                    type="text"
                    placeholder="Last Name"
                    value={lastName} // Updated to use correct state
                    onChange={(e) => setLastName(e.target.value)} // Updated handler
                />
                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default Register;