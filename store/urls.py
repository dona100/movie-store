from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, ActorViewSet, DirectorViewSet, MovieViewSet

router = DefaultRouter()
router.register(r'genre', GenreViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
