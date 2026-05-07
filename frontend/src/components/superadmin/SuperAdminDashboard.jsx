import React, { useState } from 'react';

export default function SuperAdminDashboard() {
  const [formData, setFormData] = useState({
    restaurant_name: '',
    owner_name: '',
    email: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const token = localStorage.getItem('superadmin_token');
    const API = `http://${window.location.hostname}:5000/api`;
    const res = await fetch(`${API}/superadmin/create-restaurant`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(formData)
    });
    const data = await res.json();
    if (res.ok) {
      setMsg('✅ Restaurant Admin created successfully!');
      setFormData({ restaurant_name: '', owner_name: '', email: '', password: '' });
    } else {
      setMsg(`❌ Error: ${data.message}`);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 40, maxWidth: 800, margin: '0 auto' }}>
      <h1 style={{ fontSize: 32, fontWeight: 900, marginBottom: 40 }}>Super Admin Panel</h1>

      <div className="card" style={{ padding: 40 }}>
        <h2 style={{ fontSize: 20, marginBottom: 30 }}>Add New Restaurant Partner</h2>
        {msg && <div style={{ padding: 15, borderRadius: 8, background: msg.includes('✅') ? 'rgba(29,185,84,0.1)' : 'rgba(255,0,0,0.1)', color: msg.includes('✅') ? '#1DB954' : '#FF4B4B', marginBottom: 20 }}>{msg}</div>}
        
        <form onSubmit={handleSubmit} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
          <div className="input-group">
            <label>Restaurant Name</label>
            <input value={formData.restaurant_name} onChange={e => setFormData({...formData, restaurant_name: e.target.value})} required />
          </div>
          <div className="input-group">
            <label>Owner Name</label>
            <input value={formData.owner_name} onChange={e => setFormData({...formData, owner_name: e.target.value})} required />
          </div>
          <div className="input-group">
            <label>Login Email</label>
            <input type="email" value={formData.email} onChange={e => setFormData({...formData, email: e.target.value})} required />
          </div>
          <div className="input-group">
            <label>Initial Password</label>
            <input type="password" value={formData.password} onChange={e => setFormData({...formData, password: e.target.value})} required />
          </div>
          <button type="submit" className="btn-primary" style={{ gridColumn: 'span 2', marginTop: 10 }} disabled={loading}>
            {loading ? 'Creating...' : 'Create Restaurant & Admin Account'}
          </button>
        </form>
      </div>
    </div>
  );
}
