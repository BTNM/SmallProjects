class Recipe:
    def __init__(self, name):
        """
        Initialize the Recipe object with a name, and empty lists for ingredients and instructions.
        """
        self.name = name
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, ingredient):
        """
        Add an ingredient to the ingredients list.
        
        :param ingredient: A string representing an ingredient.
        """
        self.ingredients.append(ingredient)
    
    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def add_instruction(self, instruction):
        """
        Add an instruction to the instructions list.
        
        :param instruction: A string representing a cooking instruction.
        """
        self.instructions.append(instruction)

    def remove_instruction(self, position):
        if position-1 != 0:
            del self.instructions [position-1]

    def display_recipe(self):
        """
        Display the complete recipe including the name, ingredients, and instructions.
        """
        print(f"Recipe: {self.name}\n")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f" - {ingredient}")
        print("\nInstructions:")
        for i, instruction in enumerate(self.instructions, 1):
            print(f"{i}. {instruction}")

    def __str__(self):
        """
        Return a string representation of the recipe.
        """
        recipe_str = f"Recipe: {self.name}\n\nIngredients:\n"
        recipe_str += '\n'.join(f" - {ingredient}" for ingredient in self.ingredients)
        recipe_str += "\n\nInstructions:\n"
        recipe_str += '\n'.join(f"{i + 1}. {instruction}" for i, instruction in enumerate(self.instructions))
        return recipe_str

# Example usage
if __name__ == "__main__":
    recipe = Recipe("Pancakes")
    recipe.add_ingredient("2 cups of flour")
    recipe.add_ingredient("2 tablespoons of sugar")
    recipe.add_ingredient("2 teaspoons of baking powder")
    recipe.add_ingredient("1/2 teaspoon of salt")
    recipe.add_ingredient("2 eggs")
    recipe.add_ingredient("1 1/2 cups of milk")
    recipe.add_ingredient("1/4 cup of melted butter")
    recipe.add_ingredient("chocolate")
    #recipe.remove_ingredient("chocolate")
    
    recipe.add_instruction("In a large bowl, sift together the flour, sugar, baking powder, and salt.")
    recipe.add_instruction("In another bowl, beat the eggs and then whisk in the milk and melted butter.")
    recipe.add_instruction("Pour the wet ingredients into the dry ingredients and stir until just combined.")
    recipe.add_instruction("Heat a lightly oiled griddle or frying pan over medium-high heat.")
    recipe.add_instruction("Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake.")
    recipe.add_instruction("Brown on both sides and serve hot.")
    recipe.add_instruction("mix in chocolate")
    recipe.remove_instruction(7)
    
    recipe.display_recipe()
    # Or print(recipe) to use the __str__ method



