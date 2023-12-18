import React, { useState, useEffect } from 'react';
import '../styles/styles.css';

const Loader = () => (
  <div className="loader"></div>
);

const TopNews = () => {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  let apiUrl = process.env.REACT_APP_API_URL_PROD; // Default to production URL

  if (window.location.hostname === 'localhost') {
    apiUrl = process.env.REACT_APP_API_URL_LOCAL; // Update URL for localhost
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${apiUrl}/get-news-data/`);
        const jsonData = await response.json();
        setData(jsonData);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setIsLoading(false);
      }
    };

    fetchData();
  }, [apiUrl]);

  return (
    <div className="container">
      <h1>Daily Top News</h1>
      {isLoading ? (
        <Loader />
      ) : (
        <div className="data-list">
          {data.map((item, index) => (
            <div className="data-item" key={index}>
              <h2>{item.title}</h2>
              {item.video ? (
                <iframe
                  title={item.title}
                  width="560"
                  height="315"
                  src={item.video}
                  frameBorder="0"
                  allowFullScreen
                ></iframe>
              ) : (
                <img src={item.image} alt={item.title} />
              )}
              <p>{item.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default TopNews;