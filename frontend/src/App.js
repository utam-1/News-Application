import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [headlines, setHeadlines] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchHeadlines = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/headlines/');
        setHeadlines(response.data);
      } catch (err) {
        setError('Failed to fetch news headlines');
      }
    };

    fetchHeadlines();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Latest News Headlines</h1>
      </header>
      <main>
        {error ? (
          <p className="error">{error}</p>
        ) : (
          <div className="headlines">
            {headlines.map((headline, index) => (
              <div key={index} className="headline-card">
                <h2>{headline.title}</h2>
                <p className="description">{headline.description}</p>
                <div className="meta-info">
                  <p>Source: <a href={headline.url} target="_blank" rel="noopener noreferrer">{headline.source}</a></p>
                  <p>Published: {new Date(headline.publishedAt).toLocaleString()}</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;