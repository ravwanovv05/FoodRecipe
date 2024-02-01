from django.urls import path
from api.views.comment_recipe import CommentRecipeGenericAPIView, CommentsRecipeGenericAPIView
from api.views.dish import CreateDishGenericAPIView, MyRecipeGenericAPIView
from api.views.rate_to_recipe import RateToRecipeGenericAPIView
from api.views.saved_recipe import SavedRecipeGenericAPIView, SavedRecipeDetailGenericAPIView, UnSaveRecipeAPIView
from api.views.category import CategoryGenericAPIView
from api.views.search_recipe import SearchRecipeListAPIView
from api.views.new_recipe_get import NewRecipeGetView
urlpatterns = [
    path('create-dish', CreateDishGenericAPIView.as_view(), name='create-dish'),
    path('saved-recipe', SavedRecipeGenericAPIView.as_view(), name='saved-recipe'),
    path('saved_recipe_detail/<int:pk>', SavedRecipeDetailGenericAPIView.as_view(), name='saved_recipe_detail'),
    path('unsave-recipe/<int:pk>', UnSaveRecipeAPIView.as_view(), name='unsave-recipe'),
    path('rateto-recipe', RateToRecipeGenericAPIView.as_view(), name='rateto-recipe'),
    path('search-recipe', SearchRecipeListAPIView.as_view(), name='search-recipe'),
    path('my-recipe', MyRecipeGenericAPIView.as_view(), name='my-recipe'),
    path('comment', CommentRecipeGenericAPIView.as_view(), name='comment'),
    path('comments/<int:dish_id>', CommentsRecipeGenericAPIView.as_view(), name='comments'),
    path('category/', CategoryGenericAPIView.as_view(), name='category'),
    path('create-dish', CreateDishGenericAPIView.as_view(), name='create-dish'),
    path('new-recipe-get/', NewRecipeGetView.as_view(), name='new-recipe-get')
]

