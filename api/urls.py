from django.urls import path
from api.views.category import CategoryGenericAPIView
from api.views.comment_recipe import CommentRecipeGenericAPIView, CommentsRecipeGenericAPIView
from api.views.dish import CreateDishGenericAPIView, MyRecipeGenericAPIView, MyRecipeDetailGenericAPIView
from api.views.rate_to_recipe import RateToRecipeGenericAPIView
from api.views.saved_recipe import SavedRecipeGenericAPIView, SavedRecipeDetailGenericAPIView, UnSaveRecipeAPIView, CountSavedRecipeAPIView
from api.views.search_recipe import SearchRecipeListAPIView

urlpatterns = [
    path('create-dish', CreateDishGenericAPIView.as_view(), name='create-dish'),
    path('saved-recipe', SavedRecipeGenericAPIView.as_view(), name='saved-recipe'),
    path('saved-recipe-detail/<int:dish_id>', SavedRecipeDetailGenericAPIView.as_view(), name='saved-recipe-detail'),
    path('count-saved-recipe/<int:dish_id>', CountSavedRecipeAPIView.as_view(), name='count-saved-recipe'),
    path('unsave-recipe/<int:dish_id>', UnSaveRecipeAPIView.as_view(), name='unsave-recipe'),
    path('rateto-recipe', RateToRecipeGenericAPIView.as_view(), name='rateto-recipe'),
    path('category', CategoryGenericAPIView.as_view(), name='category'),
    path('search-recipe', SearchRecipeListAPIView.as_view(), name='search-recipe'),
    path('my-recipe', MyRecipeGenericAPIView.as_view(), name='my-recipe'),
    path('my-recipe-detail/<int:dish_id>', MyRecipeDetailGenericAPIView.as_view(), name='my-recipe-detail'),
    path('comment', CommentRecipeGenericAPIView.as_view(), name='comment'),
    path('comments/<int:dish_id>', CommentsRecipeGenericAPIView.as_view(), name='comments'),
]
