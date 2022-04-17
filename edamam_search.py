import requests
from random import randint

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
    recipe_uri_hash = current_recipe_uri.rsplit('#')[1]
    print(recipe_uri_hash)
    recipe_id_url = f'https://api.edamam.com/api/recipes/v2/{recipe_uri_hash}?app_id=942811b7&app_key=20f8a29b1db2ba3778c96bfeead61d12&type=public'
    result = requests.get(recipe_id_url)
    data = result.json()

    recipe_label = (data['recipe']['label'])
    recipe_uri = (data['recipe']['uri'])
    mycursor.execute("INSERT INTO recipes (recipe_uri, recipe_label) values (%s, %s)", (recipe_uri, recipe_label))

    ingredient_items = data['recipe']['ingredients']
    length = len(ingredient_items)
    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['food'])
        mycursor.execute(f"INSERT IGNORE INTO ingredients (ingredient_label) values (\'{recipe_ingredient}\')")
        ingredient_measurement = (ingredient_items[i]['quantity'])
        mycursor.execute(f"INSERT IGNORE INTO measurement (measurement) values (\'{ingredient_measurement}\')")
        ingredient_unit = (ingredient_items[i]['measure'])
        mycursor.execute(f"INSERT IGNORE INTO units (unit) values (\'{ingredient_unit}\')")


       #ingredient_quantity = (ingredient_items[i]['quantity'])
        #ingredient_measure = (ingredient_items[i]['measure'])

    # for new_ingredient in recipe_ingredient_list:
    #     recipe_ingredient = new_ingredient
    #     sql = "INSERT INTO ingredients (ingredient_label) values (%s)"
    #     value = recipe_ingredient
    #     mycursor.execute(sql, value)





        #ingredient_quantity = (ingredient_items[i]['quantity'])
        #ingredient_measure = (ingredient_items[i]['measure'])
    # recipe_id = randint(0, 999)
    # recipe_ids[recipe_uri] = recipe_id
    # if recipe_id in recipe_ids:
    #     recipe_id = randint(1, 999)




    mydb.commit()


ingredient = input('Please enter one ingredient: ')
url = f'https://api.edamam.com/search?q={ingredient}&app_id=942811b7&app_key=20f8a29b1db2ba3778c96bfeead61d12'
result = requests.get(url)
data = result.json()
results = data['hits']


for result in results:
    current_recipe = result['recipe']
    print(f"Recipe: {current_recipe['label']}, \n{current_recipe['url'], }\n{current_recipe['ingredientLines']} \n")
    choice = input('Would you like to save this recipe? yes/no or type \'q\' to quit: ')
    if choice.lower() == 'yes':
        save_recipes(current_recipe)
        print(f"Recipe saved: {current_recipe['label']}")
    elif choice.lower() == 'q':
        break

print(results_saved)




