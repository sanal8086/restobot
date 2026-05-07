import React, { createContext, useContext, useState, useEffect } from 'react';
import { getBrowserFingerprint } from '../utils/guestUtils';
import { API_BASE_URL } from '../apiConfig';

const GuestContext = createContext();

export const useGuest = () => useContext(GuestContext);

export const GuestProvider = ({ children }) => {
    const [guest, setGuest] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const identify = async () => {
            try {
                const fingerprint = getBrowserFingerprint();
                const res = await fetch(`${API_BASE_URL}/guests/identify`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ fingerprint })
                });
                const data = await res.json();
                if (data.success) {
                    setGuest(data);
                }
            } catch (err) {
                console.error('Guest identification failed:', err);
            } finally {
                setLoading(false);
            }
        };

        identify();
    }, []);

    return (
        <GuestContext.Provider value={{ guest, loading }}>
            {children}
        </GuestContext.Provider>
    );
};
