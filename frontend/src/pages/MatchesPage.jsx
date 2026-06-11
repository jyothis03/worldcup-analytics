import React, { useState, useEffect } from 'react';
import { MatchGrid } from '../components/MatchGrid';
import { PredictionOverlay } from '../components/PredictionOverlay';
import { fetchMatches, fetchPrediction } from '../services/api';

export const MatchesPage = () => {
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [prediction, setPrediction] = useState(null);
  const [isPredicting, setIsPredicting] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadMatches = async () => {
      try {
        const data = await fetchMatches();
        setMatches(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    loadMatches();
  }, []);

  const handlePredict = async (matchId) => {
    setIsPredicting(true);
    setError(null);
    try {
      const data = await fetchPrediction(matchId);
      setPrediction(data);
    } catch (err) {
      setError(err.message || 'Failed to generate prediction');
    } finally {
      setIsPredicting(false);
    }
  };

  return (
    <div style={{ padding: '20px 0' }}>
      {isPredicting && (
        <div className="modal-overlay">
          <div className="glass-panel animate-pulse" style={{ padding: '40px', textAlign: 'center', maxWidth: '400px' }}>
            <h2 style={{ color: 'var(--accent-neon)', marginBottom: '16px' }}>Analyzing Match...</h2>
            <p style={{ color: 'var(--text-secondary)' }}>
              Gemini AI is actively researching the latest squad news, injuries, and tactical data to simulate the match. This may take up to 20 seconds.
            </p>
          </div>
        </div>
      )}

      {error && (
        <div style={{ background: 'rgba(0, 255, 136, 0.05)', border: '1px solid var(--accent-neon)', padding: '16px', margin: '20px auto', maxWidth: '600px', borderRadius: '8px', color: 'var(--text-primary)', textAlign: 'center' }}>
          {error}
          <button className="glass-button" style={{ marginLeft: '16px', padding: '6px 12px' }} onClick={() => setError(null)}>Dismiss</button>
        </div>
      )}

      {loading ? (
        <div style={{ textAlign: 'center', padding: '100px', color: 'var(--text-secondary)' }}>Loading Matches...</div>
      ) : (
        <MatchGrid matches={matches} onPredict={handlePredict} />
      )}

      <PredictionOverlay 
        prediction={prediction} 
        onClose={() => setPrediction(null)} 
      />
    </div>
  );
};
