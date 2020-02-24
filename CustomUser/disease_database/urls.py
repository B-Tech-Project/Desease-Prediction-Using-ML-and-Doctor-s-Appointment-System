from django.urls import path, include
from .views import SearchView, disease_list_view
app_name = 'disease_database'

urlpatterns = [
    path('search', SearchView, name='search'),
    path('search/submit/', disease_list_view, name='submit_symptom')
]