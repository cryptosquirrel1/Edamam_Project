import requests

def recipe_search(key_word):
    """
    displays all the credentials to access the API
    """
    APP_ID = '5ec8b15f'
    API_KEY = 'f872fab13b04a660a923e43c2e9f5654'
    url = f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={key_word}&app_id={APP_ID}&app_key={API_KEY}'
    result = requests.get(url)
    data = result.json()
    data = data['hits']
    return data

def display_recipe_results(data, index):
    """
    displays all recipe labels from the results and returns with the index numbers
    """
    print()
    # Enumerate - I learned this online. I wanted to return the index numbers of the results and display it to the console
    for index, results in enumerate(data):
        recipe = results['recipe']
        print(index, recipe['label'], '-', recipe['shareAs'])
        print('========================================')
        print(f"   Select Recipe # (0-{index})\n")
    print()
    return index

def recipe_choice(recipes):
    """
    Allows the user to select a recipe from the index.
    """
    choice = int(input("Enter a choice (number): "))  # Corrected the input prompt
    if 0 <= choice < len(recipes):  # Check if the choice is within the range of available recipes
        recipe = recipes[choice]  # Access the recipe by index
        return recipe
    else:
        print("Invalid choice. Please enter a number within the recipe index range.")
        return None

''''' BEFORE
# def save_recipe_to_file(chosen_recipe):
#     """
#     Saves the chosen recipe to a text file.
#     """
#     user_print = input('Would you like to save your recipe (y/n)? ').lower()
#     if user_print == 'y':
#         # Save the recipe in a text file
#         title = 'My Recipes'
#         filename = 'My_Recipes.txt'  # Specify the desired filename
# 
#         with open(filename, 'w+') as text_file:
#             text_file.write(title + '\n')  # Write the title to the file
#             text_file.write('Recipe Label: ' + chosen_recipe['label'] + '\n')  # Write the recipe label BUT
#             text_file.write('Cuisine: ' + chosen_recipe['cuisineType'] + '\n')  # Write the cuisine type
#             text_file.write('Ingredients:\n')
#             for ingredient in chosen_recipe['ingredientLines']:
#                 text_file.write("- " + ingredient + '\n')  # Write each ingredient line
# 
#         print(f'Successfully saved the recipe to {filename}! Yay!')
#     else:
#         print('Recipe not saved.')
'''

"AFTER "

def save_recipe_to_file(chosen_recipe):
    """
    Saves the chosen recipes to a text file.
    """
    user_print = input('Would you like to save your recipe (y/n)? ').lower()
    if user_print == 'y':
        # Save the recipe in a text file
        title = 'My Recipes'
        filename = 'My_Recipes.txt'  # Specify the desired filename

        with open(filename, 'w+') as text_file:
            text_file.write(title + '\n')  # Write the title to the file
            for label in chosen_recipe:
                label = chosen_recipe['recipe']['label']
            text_file.write('Recipe Label:' + label + '\n')  # Write the recipe label

            # cuisineType is a list and i needed to convert it to a string. Convert the list elements to a single string using ".join"
            for cuisine in chosen_recipe:
                cuisine = chosen_recipe['recipe']['cuisineType']
                cuisine_str = ', '.join(cuisine)
            text_file.write('cuisine: ' + cuisine_str + '\n')  # Write the cuisine

            text_file.write('Ingredients:' + '\n')
            for ingredients in chosen_recipe:
                ingredients = chosen_recipe['recipe']['ingredientLines']
                ingredients_str = ', '.join(ingredients)
                text_file.write(ingredients_str)  # Write each ingredient line

        print(f'Successfully saved the recipe to {filename}!!')
    else:
        print('Recipe not saved.')


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)

    for index, result in enumerate(results, start=0): # start=0 begins counting from 0
        recipe = result['recipe']
        print(f'Recipe {index}:', recipe['label'], '-', recipe['shareAs'])  # This will print the index

    print('========================================')
    print(f"   Select Recipe # (0-{index})\n")

    # Pass the list of recipes to the recipe_choice function by calling the function
    chosen_recipe = recipe_choice(results)
    if chosen_recipe:
        print('\n================================================\n')
        print("You selected:", chosen_recipe['recipe']['label'])
        print("\n================================================\n")
        print("Cuisine:", chosen_recipe['recipe']['cuisineType'])
        print("Ingredients:", chosen_recipe['recipe']['ingredientLines'])

        # Call the save_recipe_to_file function with the chosen recipe
        save_recipe_to_file(chosen_recipe)

    else:
        print("No recipe selected. Exiting...")

run()
