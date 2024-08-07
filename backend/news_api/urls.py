from django.urls import path
from .views import NewsHeadlinesView

urlpatterns = [
    path('headlines/', NewsHeadlinesView.as_view(), name='news_headlines'),
]