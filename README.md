# Top News Scraper Project

This project scrapes the top news from [news.am](https://news.am/eng/) and provides the data via a Django backend API. The frontend, built with React, displays the collected news on a single webpage.

## Prerequisites

- Docker

## Getting Started

1. Clone this repository.

    ```bash
    git clone https://github.com/ketanbamn11/news_scrapping.git
    ```

2. Navigate to the project directory.

    ```bash
    cd news_scrapping
    ```

3. Run the following commands to start the project:

    ```bash
    make build  # Start the project
    ```

    This command sets up both the Django backend and React frontend.

    Access the web page at [http://localhost:3000/](http://localhost:3000/).

## API Endpoint

To access the news data via the Django backend, use the following API endpoint:

- [http://0.0.0.0:8000/get-news-data/](http://0.0.0.0:8000/get-news-data/)

This endpoint returns the top news data in JSON format.

## Commands

- `make build`: Start the project.
- `make down`: Stop the project.

## Project Structure

- `backend/`: Django backend code for scraping news.
- `frontend/`: React frontend code for displaying news.
- `docker-compose.yml`: Docker configuration for running the project.

## Dependencies

- Django
- React
- Docker

## Notes

- Make sure Docker is installed before running the project.
