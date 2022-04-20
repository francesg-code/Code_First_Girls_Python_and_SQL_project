import requests
from dietary_requirements import options
import pprint

# Please add 'app_id' and 'add_key' credentials from your Edamam account:
# https://developer.edamam.com/edamam-recipe-api
app_id = '942811b7'
app_key = '20f8a29b1db2ba3778c96bfeead61d12'
choices = []
recipes_found = False
response_code = 000