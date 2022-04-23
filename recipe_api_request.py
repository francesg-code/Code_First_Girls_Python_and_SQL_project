import requests
from dietary_requirements import options
import edamam_search

# Please add 'app_id' and 'add_key' credentials from your Edamam account:
# https://developer.edamam.com/edamam-recipe-api
app_id = '942811b7'
app_key = '20f8a29b1db2ba3778c96bfeead61d12'
choices = []
recipes_found = False
response_code = 000
results = []

def recipe_search(url):
    """Makes the API request to Edamam, checks for errors, and either asks the user to search again
    or returns the recipe results if successful."""
    result = requests.get(url)
    global response_code
    response_code = result.status_code
    data = result.json()
    if response_code == 401:
        print('Oops! An error occurred! This may be due to invalid credentials.')
    elif not data['hits']:
        print('Sorry, no recipes found.')
    else:
        global recipes_found
        recipes_found = True
        print('Recipes found!')
        return data['hits']
    try_again = input('Would you like to try searching again? yes/no ')
    search_again(try_again)

def create_file(ingredient, choices, results):
    """Saves the recipes to a file"""
    file_name = f'{ingredient}_recipes.txt'
    with open(f'{file_name}', 'w+') as text_file:
        text_file.write('Stop staring at the fridge!' + '\n')
        text_file.write(f'Recipe ingredient: {ingredient}' + '\n')
        for item in choices:
            text_file.write('Dietary requirement: ' + item + '\n')
        for result in results:
            recipe = result['recipe']
            text_file.write('\n')
            text_file.write(recipe['label'] + '\n')
            text_file.write(recipe['url'] + '\n')
        print(f'Recipes saved to {file_name}')
        try_again = input('Would you like to try searching again? yes/no ')
        search_again(try_again)


def search_again(try_again):
    """Allows the user to search again or exit. Clears previous selections."""
    if try_again.lower() == 'yes':
        if response_code == 401:
            global app_id
            global app_key
            app_id = input('Please confirm your app_id: ')
            app_key = input('Please confirm your app_key: ')
        choices.clear()
        recipe_search_is_on()
    elif try_again.lower() == 'no' and recipes_found:
        print('Enjoy your meal! 😋')
        exit()
    else:
        print('Hope you find what you\'re looking for! Please try again soon.')
        exit()


def recipe_search_is_on():
    """Adds user's choice of ingredient and dietary requirements to the API request url."""
    print('Stop staring at the fridge! 👀👀')
    ingredient = input('Please enter one ingredient: ')
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'
    any_requirements = True
    while any_requirements:
        any_requirements_choice = input('Do you have any dietary requirements? yes/no: ')
        if any_requirements_choice.lower() == 'yes':
            any_requirements = False
            search_requirement = True
        elif any_requirements_choice.lower() == 'no':
            print(f'No dietary requirements chosen. Searching for recipes containing {ingredient} ... ')
            any_requirements = False
            search_requirement = False
        else:
            print("Please type \'yes\' or \'no\': ")

    while search_requirement:
        choice = input('Please type a dietary requirement or \'options\' to see the choices available, '
                       'or type \'done\' to search for a recipe: ')
        if choice.lower() == 'done':
            search_requirement = False
        elif choice.lower() == 'options':
            for key, value in options.items():
                print('Dietary requirement:', key, '\n', 'Description:', value)
        elif choice.lower() != 'done':
            try:
                options[choice]
            except KeyError:
                print('Sorry, please choose a dietary requirement from the choice available')
            else:
                url += f'&health={choice}'
                choices.append(choice)
                if len(choices) == 1:
                    print(f'The chosen dietary requirement is {choices}.')
                else:
                    print(f'The chosen dietary requirements are {choices}.')

    results = recipe_search(url)

    for result in results:
        current_recipe = result['recipe']
        print(f"Recipe: {current_recipe['label']}, \n{current_recipe['url'],}\n{current_recipe['ingredientLines']} \n")
        choice = input('Would you like to save this recipe? yes/no or type \'q\' to quit: ')
        if choice.lower() == 'yes':
            edamam_search.save_recipes(current_recipe)
        elif choice.lower() == 'q':
            break

recipe_search_is_on()

#print(f"Recipe saved: {recipe_api_request.current_recipe['label']}")





