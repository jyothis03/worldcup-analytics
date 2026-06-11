import React, { useState, useMemo } from 'react';
import { MatchCard } from './MatchCard';
import { ChevronLeft, ChevronRight } from 'lucide-react';

export const MatchGrid = ({ matches, onPredict }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const matchesPerPage = 10;

  // Sort chronologically and paginate
  const sortedMatches = useMemo(() => {
    if (!matches) return [];
    return [...matches].sort((a, b) => new Date(a.date) - new Date(b.date));
  }, [matches]);

  const totalPages = Math.ceil(sortedMatches.length / matchesPerPage);
  const startIndex = (currentPage - 1) * matchesPerPage;
  const currentMatches = sortedMatches.slice(startIndex, startIndex + matchesPerPage);

  if (!matches || matches.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '64px', color: 'var(--text-secondary)' }}>
        Loading match data...
      </div>
    );
  }

  return (
    <div className="glass-panel" style={{ maxWidth: '1200px', margin: '0 auto', overflow: 'hidden' }}>
      
      {/* Match Grid */}
      <div className="match-grid-container">
        {currentMatches.map((match, idx) => (
          <div key={match.id} style={{ animationDelay: `${idx * 0.05}s` }} className="animate-slide-up">
            <MatchCard match={match} onPredict={onPredict} />
          </div>
        ))}
      </div>

      {/* Pagination Footer */}
      <div style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center',
        padding: '16px 24px',
        borderTop: '1px solid var(--border-color)',
        background: 'rgba(10, 17, 13, 0.5)'
      }}>
        <div style={{ color: 'var(--text-muted)', fontSize: '13px' }}>
          Showing {startIndex + 1} to {Math.min(startIndex + matchesPerPage, sortedMatches.length)} of {sortedMatches.length} matches
        </div>
        
        <div style={{ display: 'flex', gap: '12px' }}>
          <button 
            className="glass-button" 
            style={{ display: 'flex', alignItems: 'center', gap: '4px' }}
            disabled={currentPage === 1}
            onClick={() => setCurrentPage(prev => prev - 1)}
          >
            <ChevronLeft size={16} /> Prev
          </button>
          
          <button 
            className="glass-button" 
            style={{ display: 'flex', alignItems: 'center', gap: '4px' }}
            disabled={currentPage === totalPages}
            onClick={() => setCurrentPage(prev => prev + 1)}
          >
            Next <ChevronRight size={16} />
          </button>
        </div>
      </div>
      
    </div>
  );
};
