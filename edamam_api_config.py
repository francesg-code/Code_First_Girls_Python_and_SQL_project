import requests
from dietary_requirements import options
import pprint

# Please add 'app_id' and 'add_key' credentials from your Edamam account:
# https://developer.edamam.com/edamam-recipe-api
app_id = ''
app_key = ''
choices = []
recipes_found = False
response_code = 000