from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Recipe
from api.serializers import RecipeSerializer, RecipeSerializer2
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status, generics, filters

class RecipeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeListByName(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


    # def list(self, request, *args, **kwargs):
    #     queryset =
    #CBV
class RecipeListAPIView(APIView):
     def get(self, request):
         recipies = Recipe.objects.all()
         serializer = RecipeSerializer(recipies, many=True)
         return Response(serializer.data)

     def post(self, request):
         serializer = RecipeSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RecipeDetail(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer2

    def get_queryset(self):
        name = self.kwargs['name']
        return Recipe.objects.filter(name__exact=name)


#CBV
class RecipeDetailAPIView(APIView):
    def get_object(self, recipe_id):
        try:
            return Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, recipe_id):
        # recipe = self.get_object(recipe_id)
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        serializer = RecipeSerializer(instance=recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors})

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        recipe.delete()

        return Response({'deleted': True})

#CBV
class RecipeByCategoryAPIView(APIView):
    def get(self, request, category_id):
        recipes = Recipe.objects.filter(category=category_id)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


#@api_view(['GET'])
#@permission_classes(permissions.IsAuthenticatedOrReadOnly)
#def recipe_by_name(request, name):
  #  recipes = Recipe.objects.filter(name=name)
 #   serializer = RecipeSerializer(recipes, many=True)
  #  return Response(serializer.data)

#class RecipeSearchAPIView(generics.ListCreateAPIView):
 #   search_fields = ['name']
 #   filter_backends = (filters.SearchFilter,)
 #   queryset = Recipe.objects.all()
 #   serializer_class = RecipeSerializer

@csrf_exempt
def search(request, name):
    recipes = Recipe.objects.filter(name=name)

    if request.method == 'GET':
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipes_serializer.data, safe=False)

class RecipesByCategoryAPIView(APIView):
    def get(self, request, category_id):
        recipes = Recipe.objects.filter(categoryId=category_id)
        serializer = RecipeSerializer(recipes,many=True)
        return Response(serializer.data)