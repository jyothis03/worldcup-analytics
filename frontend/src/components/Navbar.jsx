import React from 'react';
import { Trophy, Activity } from 'lucide-react';

export const Navbar = () => {
  return (
    <nav style={{
      position: 'sticky',
      top: 0,
      zIndex: 100,
      padding: '16px 32px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      borderBottom: '1px solid var(--border-color)',
      backdropFilter: 'blur(16px)',
      background: 'rgba(5, 8, 6, 0.8)'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <Trophy color="var(--accent-neon)" size={28} />
        <h1 style={{ fontSize: '24px', fontWeight: 700, margin: 0 }}>
          Tactiq<span style={{ color: 'var(--accent-neon)' }}>AI</span>
        </h1>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-secondary)' }}>
        <Activity size={18} />
        <span style={{ fontSize: '14px', fontFamily: 'Outfit', fontWeight: 500, letterSpacing: '1px', textTransform: 'uppercase' }}>Live Matrix</span>
      </div>
    </nav>
  );
};
