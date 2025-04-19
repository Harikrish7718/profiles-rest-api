from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()    
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]