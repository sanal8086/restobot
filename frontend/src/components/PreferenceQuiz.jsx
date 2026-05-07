import React, { useState } from 'react';

export default function PreferenceQuiz({ onComplete }) {
  const [step, setStep] = useState(1);
  const [prefs, setPrefs] = useState({ item_type: 'veg', spice_level: 3, heaviness: 'light' });

  const next = () => {
    if (step === 3) onComplete(prefs);
    else setStep(step + 1);
  };

  return (
    <div style={{ position: 'fixed', inset: 0, background: '#FFF', zIndex: 1000, padding: 30, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
      <div style={{ textAlign: 'center', marginBottom: 40 }}>
        <div style={{ fontSize: 12, color: '#FF6B35', fontWeight: 800, textTransform: 'uppercase', marginBottom: 10, letterSpacing: 2 }}>AI Taste Matching · Step {step}/3</div>
        <h2 style={{ fontSize: 28, fontWeight: 900, color: '#1A1A1A' }}>
          {step === 1 && "What's your preference?"}
          {step === 2 && "How much spice can you handle?"}
          {step === 3 && "How hungry are you?"}
        </h2>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 15 }}>
        {step === 1 && (
          <>
            <button onClick={() => { setPrefs({...prefs, item_type: 'veg'}); setStep(2); }} className="btn-outline" style={{ padding: 25, fontSize: 18 }}>🥦 Pure Veg</button>
            <button onClick={() => { setPrefs({...prefs, item_type: 'non-veg'}); setStep(2); }} className="btn-outline" style={{ padding: 25, fontSize: 18 }}>🍗 Non-Veg</button>
          </>
        )}
        {step === 2 && (
          [1, 2, 3, 4, 5].map(lvl => (
            <button key={lvl} onClick={() => { setPrefs({...prefs, spice_level: lvl}); setStep(3); }} className="btn-outline" style={{ padding: 15 }}>
              {'🌶️'.repeat(lvl)} {lvl === 1 ? 'Mild' : lvl === 3 ? 'Medium' : lvl === 5 ? 'Extreme' : ''}
            </button>
          ))
        )}
        {step === 3 && (
          <>
            <button onClick={() => onComplete({...prefs, heaviness: 'light'})} className="btn-outline" style={{ padding: 25, fontSize: 18 }}>🥗 Light & Fresh</button>
            <button onClick={() => onComplete({...prefs, heaviness: 'medium'})} className="btn-outline" style={{ padding: 25, fontSize: 18 }}>🍛 Balanced Meal</button>
            <button onClick={() => onComplete({...prefs, heaviness: 'heavy'})} className="btn-outline" style={{ padding: 25, fontSize: 18 }}>🥘 Heavy & Filling</button>
          </>
        )}
      </div>

      <button onClick={() => onComplete(prefs)} style={{ marginTop: 40, color: '#AAA', fontSize: 14, background: 'none', border: 'none' }}>Skip and browse full menu</button>
    </div>
  );
}
