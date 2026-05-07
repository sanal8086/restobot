import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { API_BASE_URL } from '../../apiConfig';

export default function AdminRegister() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    restaurant_name: '',
    owner_name: '',
    address: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await res.json();
      if (res.ok) {
        login(data.token, data.user);
        navigate('/admin');
      } else {
        setError(data.message);
      }
    } catch (err) {
      setError('Registration failed');
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: '100px auto', padding: 20 }} className="card">
      <h2 style={{ marginBottom: 20 }}>Register Restaurant</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: 15 }}>
        <input type="text" placeholder="Restaurant Name" required className="btn-outline" style={{ textAlign: 'left' }}
          onChange={e => setFormData({ ...formData, restaurant_name: e.target.value })} />
        <input type="text" placeholder="Owner Name" required className="btn-outline" style={{ textAlign: 'left' }}
          onChange={e => setFormData({ ...formData, owner_name: e.target.value })} />
        <input type="email" placeholder="Email" required className="btn-outline" style={{ textAlign: 'left' }}
          onChange={e => setFormData({ ...formData, email: e.target.value })} />
        <input type="password" placeholder="Password" required className="btn-outline" style={{ textAlign: 'left' }}
          onChange={e => setFormData({ ...formData, password: e.target.value })} />
        <textarea placeholder="Address" className="btn-outline" style={{ textAlign: 'left' }}
          onChange={e => setFormData({ ...formData, address: e.target.value })} />
        <button type="submit" className="btn-primary">Register</button>
      </form>
      <p style={{ marginTop: 15 }}>Already have an account? <Link to="/admin/login">Login</Link></p>
    </div>
  );
}
