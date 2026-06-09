const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

export const fetchMatches = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/matches`);
    if (!response.ok) throw new Error('Failed to fetch matches');
    const data = await response.json();
    return data.matches;
  } catch (error) {
    console.error('Error fetching matches:', error);
    return [];
  }
};

export const fetchPrediction = async (matchId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/predict?match_id=${matchId}`);
    if (!response.ok) {
      if (response.status === 503) {
        throw new Error('Gemini API is currently busy. Please try again.');
      }
      throw new Error('Prediction failed to load');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching prediction:', error);
    throw error;
  }
};
