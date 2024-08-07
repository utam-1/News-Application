import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response

class NewsHeadlinesView(APIView):
    def get(self, request):
        cache_key = 'bbc_news_headlines'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'sources': 'bbc-news',  # This specifies BBC News as the source
            'apiKey': settings.NEWS_API_KEY
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code == 200:
                articles = data.get('articles', [])[:5]  # Get first 5 articles
                headlines = [
                    {
                        'title': article['title'],
                        'source': article['source']['name'],
                        'publishedAt': article['publishedAt'],
                        'url': article['url'],
                        'description': article['description'] or "No description available"
                    }
                    for article in articles
                ]
                
                # Cache the processed data
                cache.set(cache_key, headlines, 300)  # Cache for 5 minutes
                return Response(headlines)
            else:
                # Handle API error
                return Response({'error': 'Failed to fetch news'}, status=500)
        except requests.RequestException:
            # Handle network or connection error
            return Response({'error': 'Failed to connect to the news service'}, status=500)