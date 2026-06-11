import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Trophy, Activity, ArrowRight, BrainCircuit, Globe2 } from 'lucide-react';

export const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div style={{
      minHeight: 'calc(100vh - 70px)',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '40px',
      position: 'relative',
      overflow: 'hidden'
    }}>
      {/* Background Abstract Glow */}
      <div style={{
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: '600px',
        height: '600px',
        background: 'radial-gradient(circle, rgba(0,255,136,0.15) 0%, rgba(0,0,0,0) 70%)',
        zIndex: 0,
        pointerEvents: 'none'
      }}></div>

      <div style={{ zIndex: 1, textAlign: 'center', maxWidth: '800px' }}>
        
        {/* Badges */}
        <div style={{ display: 'flex', justifyContent: 'center', gap: '16px', marginBottom: '32px' }}>
          <div style={{
            display: 'flex', alignItems: 'center', gap: '8px',
            background: 'rgba(0, 255, 136, 0.05)',
            border: '1px solid var(--border-color)',
            padding: '6px 16px',
            borderRadius: '20px',
            color: 'var(--text-secondary)',
            fontFamily: 'Outfit',
            fontSize: '14px',
            fontWeight: 600
          }}>
            <BrainCircuit size={16} /> Powered by Gemini AI
          </div>
          <div style={{
            display: 'flex', alignItems: 'center', gap: '8px',
            background: 'rgba(0, 255, 136, 0.05)',
            border: '1px solid var(--border-color)',
            padding: '6px 16px',
            borderRadius: '20px',
            color: 'var(--text-secondary)',
            fontFamily: 'Outfit',
            fontSize: '14px',
            fontWeight: 600
          }}>
            <Globe2 size={16} /> Live Web Research
          </div>
        </div>

        {/* Hero Text */}
        <h1 style={{
          fontSize: '56px',
          lineHeight: '1.1',
          marginBottom: '24px',
          background: 'linear-gradient(to right, #ffffff, var(--text-secondary))',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          textShadow: '0 0 40px rgba(0, 255, 136, 0.2)'
        }}>
          FIFA World Cup 2026 Predictions
        </h1>
        
        <p style={{
          fontSize: '20px',
          color: 'var(--text-muted)',
          marginBottom: '48px',
          lineHeight: '1.6',
          maxWidth: '600px',
          margin: '0 auto 48px auto'
        }}>
          Experience the future of sports analytics. Our elite AI engine dynamically researches squad news and generates highly accurate tactical analysis and score predictions.
        </p>

        {/* Call to Action */}
        <button 
          className="glass-button"
          style={{
            fontSize: '18px',
            padding: '16px 32px',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '12px',
            borderRadius: '8px',
            boxShadow: '0 0 20px rgba(0, 255, 136, 0.15)'
          }}
          onClick={() => navigate('/matches')}
        >
          <Activity size={20} /> Enter Dashboard <ArrowRight size={20} />
        </button>

      </div>
    </div>
  );
};
