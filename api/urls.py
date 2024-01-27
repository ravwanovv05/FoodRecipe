from django.urls import path
from api.views.dish import CreateDishGenericAPIView
from api.views.rate_to_recipe import RateToRecipeGenericAPIView
from api.views.saved_recipe import SavedRecipeGenericAPIView, SavedRecipeDetailGenericAPIView, UnSaveRecipeAPIView

urlpatterns = [
    path('create-dish', CreateDishGenericAPIView.as_view(), name='create-dish'),
    path('saved-recipe', SavedRecipeGenericAPIView.as_view(), name='saved-recipe'),
    path('saved-recipe-detail/<int:pk>', SavedRecipeDetailGenericAPIView.as_view(), name='saved-recipe-detail'),
    path('unsave-recipe/<int:pk>', UnSaveRecipeAPIView.as_view(), name='unsave-recipe'),
    path('rateto-recipe', RateToRecipeGenericAPIView.as_view(), name='rateto-recipe'),
]
