import json
from data.models.ingredient import Ingredient
from data.models.recette import RecetteIngredient


def update_scores():
    print("Updating Ecobalyse score")
    recettes_ingredients = RecetteIngredient.objects.all().select_related(
        "recette", "ingredient"
    )
    ecobalyse_ingredients = []

    for recette_ingredient in recettes_ingredients:
        print(f"{recette_ingredient.recette}")
        ecobalyse_ingredients.append(
            recette_ingredient.ingredient.id_ecobalyse
            + ";"
            + str(int(recette_ingredient.poids))
        )

    payload = {"ingredients[]": ecobalyse_ingredients}

    print(json.dumps(payload, indent=2))


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
