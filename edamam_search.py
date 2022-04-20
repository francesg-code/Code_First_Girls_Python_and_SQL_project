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
    recipe_hash = current_recipe_uri.rsplit('#')[1]
    recipe_id_url = f'https://api.edamam.com/api/recipes/v2/{recipe_hash}?app_id=942811b7&app_key=20f8a29b1db2ba3778c96bfeead61d12&type=public'
    recipe_uri_hash = current_recipe_uri.rsplit('#')[1]
    recipe_id_url = f'https://api.edamam.com/api/recipes/v2/{recipe_uri_hash}?app_id=&app_key=&type=public'
    result = requests.get(recipe_id_url)
    data = result.json()

    ingredient_ids = {}
    measurement_ids = {}
    unit_ids = {}
    dietary_requirements_ids = {}

    recipe_label = (current_recipe['label'])
    #recipe_uri = (data['recipe']['uri'])
    mycursor.execute("INSERT INTO recipes (recipe_hash, recipe_label) values (%s, %s)", (recipe_hash, recipe_label))
    mycursor.execute(f"SELECT recipe_id FROM recipes WHERE recipe_hash = (\'{recipe_hash}\')")
    recipe_id = mycursor.fetchall()
    print(recipe_id)
    ingredient_items = current_recipe['ingredients']
    length = len(ingredient_items)
    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['food'])
        mycursor.execute(f"INSERT IGNORE INTO ingredients (ingredient) values (\'{recipe_ingredient}\')")

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['food'])
        mycursor.execute(f"SELECT ingredient_id FROM ingredients WHERE ingredient = \'{recipe_ingredient}\'")
        ingredient_id_result = mycursor.fetchall()
        ingredient_ids[recipe_ingredient] = ingredient_id_result

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['quantity'])
        mycursor.execute(f"INSERT IGNORE INTO measurements (measurement) values (\'{recipe_ingredient}\')")

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['quantity'])
        mycursor.execute(f"SELECT measurement_id FROM measurements WHERE measurement = \'{recipe_ingredient}\'")
        measurement_id_result = mycursor.fetchall()
        measurement_ids[recipe_ingredient] = measurement_id_result

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['measure'])
        mycursor.execute(f"INSERT IGNORE INTO units (unit) values (\'{recipe_ingredient}\')")

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['measure'])
        mycursor.execute(f"SELECT unit_id FROM units WHERE unit = \'{recipe_ingredient}\'")
        unit_id_result = mycursor.fetchall()
        unit_ids[recipe_ingredient] = unit_id_result

    print(f"Recipe ID: ", recipe_id)

    print(f"Ingredient_ID :", ingredient_ids)
    print("Mesasurmet IDS: ", measurement_ids)
    print("Unit IDS: ", unit_ids)
    mydb.commit()

    # for i in ingredient_ids.values():
    #     mycursor.execute(f"INSERT INTO recipe_ingredients (recipe_id, ingredient_id) values (\'{recipe_id}\', \'{i}\')")
    #
    # for m in measurement_ids.values():
    #     mycursor.execute(f"INSERT INTO recipe_ingredients (recipe_id, measurement_id) values (\'{recipe_id}\', \'{m}\')")
    #
    # for u in unit_ids.values():
    #     mycursor.execute(f"INSERT INTO recipe_ingredients (recipe_id, unit_id) values (\'{recipe_id}\', \'{u}\')")
    #

    maybe values saved to nested dict and then can loop over main dict e.g. for i in recipes[recipe][i]
    for i in range(length):
        mycursor.execute(f"INSERT INTO recipe_ingredients (recipe_id, ingredient_id, measurement_id) values (\'{recipe_id}\', \'{ingredient_ids[i]}\', \'{measurement_ids[i]}\', \'{unit_ids[i]}\'))")

    mydb.commit()










    # recipe_label = (data['recipe']['label'])
    # #recipe_uri = (data['recipe']['uri'])
    # mycursor.execute("INSERT INTO recipes (recipe_hash, recipe_label) values (%s, %s)", (recipe_uri_hash, recipe_label))
    # description = data['recipe']['ingredientLines']
    # description_str = ', '.join(description)
    # mycursor.execute("INSERT IGNORE INTO recipe_ingredients (recipe_hash, description) values (%s, %s)", (recipe_uri_hash, description_str))
    # mydb.commit()


        #
        #
        # ingredient_measurement = (ingredient_items[i]['quantity'])
        # mycursor.execute(f"INSERT IGNORE INTO measurements (measurement) values (\'{ingredient_measurement}\')")
        # mydb.commit()
        # # mycursor.execute("SELECT measurement_id FROM measurements")
        # # measurement_id = mycursor.fetchall()
        #
        #
        # ingredient_unit = (ingredient_items[i]['measure'])
        # mycursor.execute(f"INSERT IGNORE INTO units (unit) values (\'{ingredient_unit}\')")
        # mydb.commit()
        # # mycursor.execute("SELECT unit_id FROM units")
        # # unit_id = mycursor.fetchall()


        # mycursor.execute(f"INSERT INTO recipe_ingredients (recipe_id, ingredient_id, measurement_id, unit_id )"
        #                                       f" values (%s, %s, %s, %s)", (recipe_id, ingredient_id, measurement_id, unit_id))






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




