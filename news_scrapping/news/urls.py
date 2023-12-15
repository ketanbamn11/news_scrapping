from django.urls import path
from .views import NewsDataView

urlpatterns = [
    path('get-news-data/', NewsDataView.as_view(), name='get-news-data'),
]
