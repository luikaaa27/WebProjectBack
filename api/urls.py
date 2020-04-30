from django.urls import path
from .Views.recipe import *
from .Views.user import UserCreateAPIView, logout, UserList, CurrentUserProfile
from .Views.category import category_list, CategoryList, category_detail, VacancyByCompanyAPIView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('recipes/', RecipeListAPIView.as_view(), name='RecipeList'),
    path('login/', obtain_jwt_token, name='ObtainJWTToken'),
    path('signup/', UserCreateAPIView.as_view(), name='Sign-Up'),
    path('logout/', logout, name='logout'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path(r'categories/<int:category_id>/', category_detail, name='CategoryDetail'),
    path(r'categories/<int:category_id>/recipes/',VacancyByCompanyAPIView.as_view() , name='CategoryRecipes'),
    path(r'user/profile/', CurrentUserProfile.as_view(), name='UserProfile'),
    path('user-list/', UserList.as_view(), name='User-List'),
    path('recipes/search/<str:name>/', search, name='RecipeListByName'),
    path('recipes/<int:recipe_id>/', RecipeDetailAPIView.as_view(), name='one recipe'),
]