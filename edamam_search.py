

    recipe_label = (data['recipe']['label'])
    #recipe_uri = (data['recipe']['uri'])
    mycursor.execute("INSERT INTO recipes (recipe_hash, recipe_label) values (%s, %s)", (recipe_hash, recipe_label))
    mycursor.execute(f"SELECT recipe_id FROM recipes WHERE recipe_hash = (\'{recipe_hash}\')")
    recipe_ids = mycursor.fetchall()
    print(recipe_ids)
    ingredient_items = data['recipe']['ingredients']
    length = len(ingredient_items)
    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['food'])
        mycursor.execute(f"INSERT IGNORE INTO ingredients (ingredient, recipe_hash) values (\'{recipe_ingredient}\', \'{recipe_hash}\')")
        #recipe_id = mycursor.execute("SELECT recipe_id FROM recipes WHERE recipe_uri = ?", (recipe_hash))

    for i in range(length):
        recipe_ingredient = (ingredient_items[i]['food'])
        mycursor.execute(f"SELECT ingredient_id FROM ingredients WHERE ingredient = \'{recipe_ingredient}\'")
        id_result = mycursor.fetchall()
        ingredient_ids[recipe_ingredient] = id_result
    print(recipe_ids)
    print(ingredient_ids)
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




