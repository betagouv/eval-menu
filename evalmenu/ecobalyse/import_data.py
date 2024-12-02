import json
from data.models.ingredient import Ingredient


def import_ingredients(ingredients_filepath: str):
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
