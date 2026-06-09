import React from 'react';
import { Calendar, MapPin, Activity } from 'lucide-react';

export const MatchCard = ({ match, onPredict }) => {
  const dateObj = new Date(match.date);
  const dateStr = dateObj.toLocaleDateString('en-US', { month: 'short', day: '2-digit' });
  const timeStr = dateObj.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

  return (
    <div className="data-row" style={{ cursor: 'pointer' }} onClick={() => onPredict(match.id)}>
      
      {/* Date & Time */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--text-primary)' }}>
          <Calendar size={14} color="var(--text-secondary)" />
          <span style={{ fontWeight: 500 }}>{dateStr}</span>
        </div>
        <span style={{ color: 'var(--text-muted)', fontSize: '12px', paddingLeft: '20px' }}>
          {timeStr}
        </span>
      </div>

      {/* Matchup */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
        <span style={{ fontWeight: 600, fontSize: '15px', color: 'var(--text-primary)', width: '140px', textAlign: 'right' }}>
          {match.home_team}
        </span>
        <span style={{ color: 'var(--text-muted)', fontSize: '12px', fontWeight: 600 }}>VS</span>
        <span style={{ fontWeight: 600, fontSize: '15px', color: 'var(--text-primary)', width: '140px' }}>
          {match.away_team}
        </span>
      </div>

      {/* Group */}
      <div>
        <span style={{ 
          background: 'rgba(0, 255, 136, 0.05)', 
          color: 'var(--accent-neon)', 
          padding: '4px 8px', 
          borderRadius: '4px', 
          fontFamily: 'Outfit',
          fontSize: '12px',
          fontWeight: 500,
          border: '1px solid var(--border-color)'
        }}>
          {match.group}
        </span>
      </div>

      {/* Location */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--text-secondary)' }}>
        <MapPin size={14} />
        <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{match.venue}</span>
      </div>

      {/* Action */}
      <div style={{ textAlign: 'right' }}>
        <button 
          className="glass-button" 
          style={{ padding: '6px 12px', fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', marginLeft: 'auto' }}
          onClick={(e) => { e.stopPropagation(); onPredict(match.id); }}
        >
          <Activity size={14} /> Analyze
        </button>
      </div>

    </div>
  );
};
