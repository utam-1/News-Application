# News Headlines Application

Welcome to the News Headlines Application repository! This dashboard provides the latest news headlines with a clean and user-friendly interface.

## About

This application leverages the power of React.js for the frontend and Django for the backend to provide a seamless and interactive experience for viewing the latest news headlines. The application fetches data from the News API, displays it in an appealing format, and includes caching to optimize performance.

## Tech Stack

- Frontend:
  - React.js: A JavaScript library for building user interfaces
  - Axios: Promise-based HTTP client for making API requests

- Backend:
  - Django: A high-level Python web framework
  - Django Rest Framework: A powerful and flexible toolkit for building Web APIs
  - Requests: A simple HTTP library for Python

- API:
  - News API: Provides access to breaking news headlines and articles from over 80,000 sources

## Features

- Displays the latest 5 news headlines
- Shows article title, description, source, and publication date
- Provides a link to the full article
- Implements caching to reduce API calls
- Responsive and visually appealing design

## Installation
---
**NOTE**

The below steps assume that you have Python and Node.js installed on your system. If you haven't installed them, please do
so before proceeding with the below steps.

---

To get started with the News Headlines Application:

1. Clone this repository: `git clone https://github.com/utam-1/News-application `

2. Set up the backend:
```
cd news-website/backend
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt

```

3. Set up the frontend:

``` 
cd ../frontend
npm install

```

4. Configure your own News API:
---
**NOTE**

An API key has already been provided configured to be used if application is run in development phase. 
Should you wish to test the application in production, you would need to upgrade to a paid plan of News API.

---
- Sign up for an API key at [newsapi.org](https://newsapi.org/)
- In the backend directory go to news_project\settings.py file and add your API key:
  ```
  NEWS_API_KEY=your_api_key_here

  ```

5. Run the application:
- Backend:
  ```
  cd ../backend
  python manage.py runserver
  ```
- Frontend (in a new terminal):
  ```
  cd ../frontend
  npm start
  ```

6. Open your browser and access the dashboard at [http://localhost:3000](http://localhost:3000)

## Usage

The application will automatically load the latest news headlines. Each headline card includes:
- The article title
- A brief description or excerpt
- The news source (clickable, redirects to the full article)
- The publication date and time

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
