import React from 'react';
import { X, AlertTriangle, Shield } from 'lucide-react';

export const PredictionOverlay = ({ prediction, onClose }) => {
  if (!prediction) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content glass-panel animate-slide-up" onClick={e => e.stopPropagation()} style={{ padding: '32px' }}>
        <button className="close-btn" onClick={onClose}><X size={24} /></button>
        
        <h2 style={{ color: 'var(--accent-neon)', textAlign: 'center', marginBottom: '8px', fontSize: '28px', textTransform: 'uppercase', letterSpacing: '2px' }}>Tactical Analysis</h2>
        <p style={{ textAlign: 'center', color: 'var(--text-secondary)', marginBottom: '32px' }}>
          {prediction.home_team.name} vs {prediction.away_team.name}
        </p>

        {/* Score Prediction */}
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '32px', marginBottom: '40px' }}>
          <div style={{ textAlign: 'right' }}>
            <h3 style={{ fontSize: '24px' }}>{prediction.home_team.name}</h3>
          </div>
          <div style={{ fontSize: '48px', fontWeight: 700, fontFamily: 'Outfit', color: 'var(--accent-neon)', borderBottom: '2px solid var(--border-color)', padding: '0 24px' }}>
            {prediction.predicted_score.home} - {prediction.predicted_score.away}
          </div>
          <div style={{ textAlign: 'left' }}>
            <h3 style={{ fontSize: '24px' }}>{prediction.away_team.name}</h3>
          </div>
        </div>

        {/* Win Probability Bar */}
        <div style={{ marginBottom: '40px', background: 'rgba(0,0,0,0.5)', padding: '24px', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
          <h4 style={{ marginBottom: '16px', color: 'var(--text-muted)', fontSize: '12px', textTransform: 'uppercase', letterSpacing: '1px' }}>Win Probability Model</h4>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px', fontSize: '14px', fontFamily: 'Outfit' }}>
            <span style={{ color: 'var(--text-primary)' }}>{prediction.home_team.name}: {Math.round(prediction.win_probability.home * 100)}%</span>
            <span style={{ color: 'var(--text-muted)' }}>Draw: {Math.round(prediction.win_probability.draw * 100)}%</span>
            <span style={{ color: 'var(--text-primary)' }}>{prediction.away_team.name}: {Math.round(prediction.win_probability.away * 100)}%</span>
          </div>
          <div style={{ height: '8px', display: 'flex', borderRadius: '4px', overflow: 'hidden', background: 'rgba(255,255,255,0.05)' }}>
            <div style={{ width: `${prediction.win_probability.home * 100}%`, background: 'var(--accent-neon)' }} />
            <div style={{ width: `${prediction.win_probability.draw * 100}%`, background: 'var(--text-muted)' }} />
            <div style={{ width: `${prediction.win_probability.away * 100}%`, background: 'var(--accent-dark)' }} />
          </div>
        </div>

        {/* Two Columns for Team Info */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px', marginBottom: '32px' }}>
          {[prediction.home_team, prediction.away_team].map((team, idx) => (
            <div key={idx} style={{ background: 'rgba(0, 255, 136, 0.03)', padding: '20px', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
              <h4 style={{ color: 'var(--accent-neon)', marginBottom: '16px', fontSize: '18px', display: 'flex', justifyContent: 'space-between' }}>
                {team.name}
                <span style={{ fontSize: '12px', color: 'var(--text-muted)', fontFamily: 'Outfit' }}>{team.expected_formation}</span>
              </h4>
              
              <div style={{ marginBottom: '16px' }}>
                <span style={{ color: 'var(--text-secondary)', fontSize: '11px', textTransform: 'uppercase', letterSpacing: '1px' }}>Key Players</span>
                <p style={{ fontSize: '14px', marginTop: '4px' }}>{team.key_players.join(', ')}</p>
              </div>

              {team.injuries && team.injuries.length > 0 && (
                <div>
                  <span style={{ color: 'var(--text-secondary)', fontSize: '11px', textTransform: 'uppercase', letterSpacing: '1px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <AlertTriangle size={12} color="var(--accent-neon)" /> Fitness Doubts
                  </span>
                  <ul style={{ fontSize: '13px', marginTop: '4px', color: 'var(--text-primary)', paddingLeft: '16px' }}>
                    {team.injuries.map((inj, i) => (
                      <li key={i}>{inj.player_name}: <span style={{ color: 'var(--text-muted)' }}>{inj.injury_detail}</span></li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Reasoning */}
        <div style={{ borderTop: '1px solid var(--border-color)', paddingTop: '24px' }}>
          <h4 style={{ color: 'var(--accent-neon)', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '8px', textTransform: 'uppercase', fontSize: '14px', letterSpacing: '1px' }}>
            <Shield size={16} /> Analyst Verdict
          </h4>
          <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, fontSize: '15px' }}>{prediction.reasoning}</p>
        </div>
      </div>
    </div>
  );
};
