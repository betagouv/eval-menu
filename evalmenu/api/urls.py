from django.urls import path
from api.view.recette import RecetteView

app_name = 'api'

urlpatterns = [
    path("recettes/", RecetteView.as_view(), name="recettes")
]