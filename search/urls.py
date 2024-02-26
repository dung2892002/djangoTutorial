from django.urls import path
from search.views import results

urlpatterns = [
    path('', results, name='search_results'),
]