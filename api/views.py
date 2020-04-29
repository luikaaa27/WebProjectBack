# from django.shortcuts import render
# from .models import Categories, Recipe
# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, status
# from .serializers import RecipeSerializer, UserSerializer, CategorySerializer
# from rest_framework.decorators import api_view, APIView
# from django.http import Http404
# from rest_framework.response import Response
# # Create your Views here.
#
#
# class RecipeList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#
#
# class UserCreateAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]
#
#
# # @api_view(["GET"])
# # def category_recipes(request):
# #     recipes = []
# #     category = Categories.objects.all()
# #     for c in category:
# #         for recipe in c:
# #             recipes.append(recipe)
# #     serializer = RecipeSerializer(recipes, many=True)
# #     return Response(serializer.data)
#
# class UserCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]
#
#
# # @api_view(["GET"])
# # def category_recipes(request):
# #     recipes = []
# #     category = Categories.objects.all()
# #     for c in category:
# #         for recipe in c:
# #             recipes.append(recipe)
# #     serializer = RecipeSerializer(recipes, many=True)
# #     return Response(serializer.data)
#
#
# class CategoriesAPIView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer
#
#
# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = Categories.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, category_id):
#     try:
#         category = Categories.objects.get(id=category_id)
#     except Categories.DoesNotExist as e:
#         return Response({'error': str(e)})
#
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CategorySerializer(instance=category, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.update(serializer.instance, request.data)
#             return Response(serializer.data)
#         return Response({'error': serializer.errors})
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response({'deleted': True})
#
#
# class RecipeListAPIView(APIView):
#     def get(self, request):
#         recipies = Recipe.objects.all()
#         serializer = RecipeSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = RecipeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# class RecipeDetailAPIView(APIView):
#     def get_object(self, recipe_id):
#         try:
#             return Recipe.objects.get(id=recipe_id)
#         except Recipe.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def get(self, request, recipe_id):
#         recipe = self.get_object(recipe_id)
#         serializer = RecipeSerializer(recipe)
#         return Response(serializer.data)
#
#     def put(self, request, recipe_id):
#         recipe = self.get_object(recipe_id)
#         serializer = RecipeSerializer(instance=recipe, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({'errors': serializer.errors})
#
#     def delete(self, request, recipe_id):
#         recipe = self.get_object(recipe_id)
#         recipe.delete()
#
#         return Response({'deleted': True})
#
#
# class RecipeByCategoryAPIView(APIView):
#     def get(self, request, category_id):
#         recipes = Recipe.objects.filter(category=category_id)
#         serializer = RecipeSerializer(recipes, many=True)
#         return Response(serializer.data)
#
#
# class Logout(APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
