import React, { useState, useEffect } from 'react';
import '../styles/styles.css';

const Loader = () => (
  <div className="loader"></div>
);

const TopNews = () => {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetch('http://52.207.228.88:8000/get-news-data/')
      .then(response => response.json())
      .then(data => {
        setData(data);
        setIsLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setIsLoading(false);
      });
  }, []);

  return (
    <div className="container">
      <h1>Daily Top News</h1>
      {isLoading ? (
        <Loader /> // Show loader component if loading
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
