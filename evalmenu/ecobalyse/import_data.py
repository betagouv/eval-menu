import json
import requests
from data.models.ingredient import Ingredient
from data.models.recette import RecetteIngredient, Recette
from evalmenu import settings


def update_scores():
    recettes = Recette.objects.all()
    for recette in recettes:
        update_score_for_recette(recette)


def update_score_for_recette(recette: Recette):
    print(f"Updating Ecobalyse score, for recette_id: {recette.id}")
    recettes_ingredients = RecetteIngredient.objects.filter(
        recette_id=recette.id
    ).select_related("recette", "ingredient")
    ecobalyse_ingredients = []

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    for recette_ingredient in recettes_ingredients:
        print(f"{recette_ingredient.recette} - {recette_ingredient.ingredient}")
        ecobalyse_ingredients.append(
            {
                "id": recette_ingredient.ingredient.id_ecobalyse,
                "mass": int(recette_ingredient.poids),
            }
        )

    payload = {"ingredients": ecobalyse_ingredients}

    response = requests.post(settings.ECOBALYSE_API, headers=headers, json=payload)
    if response.status_code == 200:
        score = response.json()["results"]["total"]["ecs"]
        print(f"ECS score: {score}")
        recette.cs = score
        recette.save()


def import_ingredients(ingredients_filepath: str):
    # Available at https://github.com/MTES-MCT/ecobalyse/blob/cb5e131f15a0d00178759ebe945398425a995bc8/public/data/food/ingredients.json
    print(f"Importing ecobalyse ingredients from {ingredients_filepath}")

    with open(ingredients_filepath) as f:
        ingredients = json.load(f)
        inserted_names = {}
        ingredients_to_insert = []

        for eco_ingredient in ingredients:
            name = eco_ingredient["name"]
            # Don't import ingredients hidden in Ecobalyse
            if eco_ingredient["visible"]:
                print(f"-> {name}")

                # Manage ingredients with the same name and
                # append the occurence number to the name
                if name in inserted_names:
                    new_count = inserted_names[name] + 1
                    inserted_names[name] = new_count
                    name = name + "-" + str(new_count)
                else:
                    inserted_names[name] = 0

                ingredient = Ingredient(name=name, id_ecobalyse=eco_ingredient["id"])
                ingredients_to_insert.append(ingredient)

        Ingredient.objects.bulk_create(ingredients_to_insert)
