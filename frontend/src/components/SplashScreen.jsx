import React, { useEffect, useRef, useState } from 'react';

export default function SplashScreen({ onComplete }) {
  const videoRef = useRef(null);
  const [fading, setFading] = useState(false);

  const finish = () => {
    setFading(true);
    setTimeout(onComplete, 700);
  };

  useEffect(() => {
    const timer = setTimeout(finish, 6000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className={`splash-container ${fading ? 'splash-fade-out' : ''}`}>
      <video
        ref={videoRef}
        className="splash-video"
        autoPlay muted playsInline
        onEnded={finish}
      >
        <source src="/splash.mp4" type="video/mp4" />
      </video>
      <div style={{
        position: 'absolute', bottom: 48, left: '50%',
        transform: 'translateX(-50%)', textAlign: 'center'
      }}>
        <div style={{ display: 'flex', gap: 6, justifyContent: 'center', marginBottom: 12 }}>
          {[0,1,2].map(i => (
            <div key={i} style={{
              width: 6, height: 6, borderRadius: '50%',
              background: i === 0 ? '#FF6B35' : 'rgba(255,255,255,0.3)',
              animation: `pulse 1.2s ease ${i * 0.2}s infinite`
            }} />
          ))}
        </div>
        <p style={{ color: 'rgba(255,255,255,0.5)', fontSize: 12, letterSpacing: 3, textTransform: 'uppercase' }}>
          Loading Experience
        </p>
      </div>
    </div>
  );
}
