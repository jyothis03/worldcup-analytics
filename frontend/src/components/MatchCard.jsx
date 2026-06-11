import React from 'react';
import { Calendar, MapPin, Activity } from 'lucide-react';

export const MatchCard = ({ match, onPredict }) => {
  const dateObj = new Date(match.date);
  const dateStr = dateObj.toLocaleDateString('en-US', { month: 'short', day: '2-digit' });
  const timeStr = dateObj.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

  return (
    <div className="match-card" onClick={() => onPredict(match.id)}>
      
      {/* Header: Date and Group */}
      <div className="match-card-header">
        <div className="match-card-date">
          <div className="match-card-date-main">
            <Calendar size={14} color="var(--text-secondary)" />
            <span>{dateStr}</span>
          </div>
          <span className="match-card-date-sub">{timeStr}</span>
        </div>
        <div className="match-card-group-pill">
          {match.group}
        </div>
      </div>

      {/* Body: Teams */}
      <div className="match-card-body">
        <span className="match-card-team">{match.home_team}</span>
        <span className="match-card-vs">VS</span>
        <span className="match-card-team">{match.away_team}</span>
      </div>

      {/* Footer: Venue and Action */}
      <div className="match-card-footer">
        <div className="match-card-venue">
          <MapPin size={14} />
          <span>{match.venue}</span>
        </div>
        
        <button 
          className="glass-button" 
          style={{ padding: '6px 16px', display: 'flex', alignItems: 'center', gap: '8px' }}
          onClick={(e) => { e.stopPropagation(); onPredict(match.id); }}
        >
          <Activity size={14} /> Analyze
        </button>
      </div>

    </div>
  );
};
