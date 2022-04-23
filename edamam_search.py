import requests
import recipe_api_request

import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="132674root",
    port="3306",
    db="python_cookbook"
)

mycursor = mydb.cursor()

recipe_ids = {}
results_saved = []



def save_recipes(current_recipe):
    """Make a seperate API request for the recipe that is to be saved, and adds those values to the database.  """
    current_recipe_uri = current_recipe['uri']
    recipe_hash = current_recipe_uri.rsplit('#')[1]
    recipe_id_url = f'https://api.edamam.com/api/recipes/v2/{recipe_hash}?app_id=942811b7&app_key=20f8a29b1db2ba3778c96bfeead61d12&type=public'
    recipe_uri_hash = current_recipe_uri.rsplit('#')[1]
    recipe_id_url = f'https://api.edamam.com/api/recipes/v2/{recipe_uri_hash}?app_id=&app_key=&type=public'
    result = requests.get(recipe_id_url)
    data = result.json()

    saved_recipes = {
        'recipe': {
            'recipe_id': ' ',
            'ingredient_id': [],
            'measurement_id': [],
            'unit_id': []
    }
    }

    recipe_label = (current_recipe['label'])
    recipe_url = (current_recipe['url'])
    mycursor.execute("INSERT INTO recipes (recipe_hash, recipe_label, recipe_url) values (%s, %s, %s)", (recipe_hash, recipe_label, recipe_url))
    mycursor.execute(f"SELECT recipe_id FROM recipes WHERE recipe_hash = (\'{recipe_hash}\')")
    recipe_id = mycursor.fetchall()
    for x in recipe_id:
        saved_recipes['recipe']['recipe_id'] = x[0]
    ingredient_items = current_recipe['ingredients']
    length = len(ingredient_items)
    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['food'])
        mycursor.execute(f"INSERT IGNORE INTO ingredients (ingredient) values (\'{recipe_ingredient}\')")

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['food'])
        mycursor.execute(f"SELECT ingredient_id FROM ingredients WHERE ingredient = \'{recipe_ingredient}\'")
        ingredient_id_result = mycursor.fetchall()
        for x in ingredient_id_result:
            saved_recipes['recipe']['ingredient_id'].append(x[0])

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['quantity'])
        mycursor.execute(f"INSERT IGNORE INTO measurements (measurement) values (\'{recipe_ingredient}\')")

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['quantity'])
        mycursor.execute(f"SELECT measurement_id FROM measurements WHERE measurement = \'{recipe_ingredient}\'")
        measurement_id_result = mycursor.fetchall()
        for x in measurement_id_result:
            saved_recipes['recipe']['measurement_id'].append(x[0])

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['measure'])
        mycursor.execute(f"INSERT IGNORE INTO units (unit) values (\'{recipe_ingredient}\')")

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['measure'])
        mycursor.execute(f"SELECT unit_id FROM units WHERE unit = \'{recipe_ingredient}\'")
        unit_id_result = mycursor.fetchall()
        for x in unit_id_result:
            saved_recipes['recipe']['unit_id'].append(x[0])

    print(saved_recipes)

    recipe_id = saved_recipes['recipe']['recipe_id']

    for i in range(length):
        ingredient_id = saved_recipes['recipe']['ingredient_id'][i]
        measurement_id = saved_recipes['recipe']['measurement_id'][i]
        unit_id = saved_recipes['recipe']['unit_id'][i]
        mycursor.execute(f"INSERT INTO recipe_ingredients (recipe_id, ingredient_id, measurement_id, unit_id) values (\'{recipe_id}\', \'{ingredient_id}\', \'{measurement_id}\', \'{unit_id}\')")

    mydb.commit()










# ingredient = input('Please enter one ingredient: ')
# url = f'https://api.edamam.com/search?q={ingredient}&app_id=942811b7&app_key=20f8a29b1db2ba3778c96bfeead61d12'
# result = requests.get(url)
# data = result.json()
# results = data['hits']

#
# for result in results:
#     current_recipe = result['recipe']
#     print(f"Recipe: {current_recipe['label']}, \n{current_recipe['url'], }\n{current_recipe['ingredientLines']} \n")
#     choice = input('Would you like to save this recipe? yes/no or type \'q\' to quit: ')
#     if choice.lower() == 'yes':
#         save_recipes(current_recipe)
#         print(f"Recipe saved: {current_recipe['label']}")
#     elif choice.lower() == 'q':
#         break






