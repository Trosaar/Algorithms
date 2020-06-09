#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	
	total_batches = 999999

	for ingr, vals in recipe.items():
		if ingr not in ingredients:
			ingredients[ingr] = 0

		if ingredients[ingr] // recipe[ingr] < total_batches:
			total_batches = ingredients[ingr] // recipe[ingr]

	return total_batches


if __name__ == '__main__':
	# Change the entries of these dictionaries to test 
	# your implementation with different inputs
	recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
	ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
	print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))