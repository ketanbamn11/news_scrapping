import React, { useState, useEffect } from 'react';
import '../styles/styles.css';

const TopNews = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch data from your Django endpoint
    fetch('http://0.0.0.0:8000/get-news-data/')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);
  return (
    <div className="container">
        <h1>Daily Top News</h1>
          <div className="data-list">
            {data.map((item, index) => (
              <div className="data-item" key={index}>
                <h2>{item.title}</h2>
                <img src={item.image} alt={item.title} />
                <p>{item.description}</p>
              </div>
            ))}
          </div>
        </div>
      );
};

export default TopNews;