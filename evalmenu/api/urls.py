from django.urls import path

from api.view.recette import RecetteView
from rest_framework.routers import DefaultRouter
app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    *router.urls,  # Make sure router URLs are included here
    path('recette/', RecetteView.as_view(), name="recette"),
]
