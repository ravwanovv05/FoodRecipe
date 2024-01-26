from django.urls import path
from api.views.category import CategoryAPIView
from api.views.search import SearchRecipeAPIView

urlpatterns = [
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('search-recipe/', SearchRecipeAPIView.as_view(), name='search_recipe'),
]
