from django.urls import path
from api.view.recette import RecetteViewSet
from rest_framework.routers import DefaultRouter
app_name = 'api'

router = DefaultRouter()
router.register(r'recette', RecetteViewSet)  # Ensure 'yourmodel' matches your endpoint name

urlpatterns = [
    *router.urls,  # Make sure router URLs are included here
]