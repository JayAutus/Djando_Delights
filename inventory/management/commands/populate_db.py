from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from inventory.models import Ingredient, MenuItem, RecipeRequirement


class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        # Create a default user if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created admin user'))

        # Clear existing data
        RecipeRequirement.objects.all().delete()
        MenuItem.objects.all().delete()
        Ingredient.objects.all().delete()

        # Create ingredients
        ingredients_data = [
            {'name': 'Ground Beef', 'quantity': 10.0, 'unit': 'lbs', 'price_per_unit': 5.99},
            {'name': 'Lettuce', 'quantity': 5.0, 'unit': 'heads', 'price_per_unit': 1.50},
            {'name': 'Tomato', 'quantity': 15.0, 'unit': 'units', 'price_per_unit': 0.75},
            {'name': 'Burger Buns', 'quantity': 20.0, 'unit': 'units', 'price_per_unit': 0.50},
            {'name': 'Cheese', 'quantity': 3.0, 'unit': 'lbs', 'price_per_unit': 4.99},
            {'name': 'Chicken Breast', 'quantity': 8.0, 'unit': 'lbs', 'price_per_unit': 6.99},
            {'name': 'Pasta', 'quantity': 5.0, 'unit': 'lbs', 'price_per_unit': 2.50},
            {'name': 'Tomato Sauce', 'quantity': 10.0, 'unit': 'cans', 'price_per_unit': 2.00},
            {'name': 'Mozzarella', 'quantity': 2.0, 'unit': 'lbs', 'price_per_unit': 5.99},
            {'name': 'Bacon', 'quantity': 3.0, 'unit': 'lbs', 'price_per_unit': 7.99},
        ]

        for data in ingredients_data:
            Ingredient.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(ingredients_data)} ingredients'))

        # Create menu items
        menu_items_data = [
            {'title': 'Classic Burger', 'price': 8.99},
            {'title': 'Cheeseburger', 'price': 9.99},
            {'title': 'Bacon Cheeseburger', 'price': 11.99},
            {'title': 'Chicken Sandwich', 'price': 7.99},
            {'title': 'Pasta Marinara', 'price': 10.99},
        ]

        for data in menu_items_data:
            MenuItem.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(menu_items_data)} menu items'))

        # Create recipe requirements
        beef = Ingredient.objects.get(name='Ground Beef')
        lettuce = Ingredient.objects.get(name='Lettuce')
        tomato = Ingredient.objects.get(name='Tomato')
        buns = Ingredient.objects.get(name='Burger Buns')
        cheese = Ingredient.objects.get(name='Cheese')
        chicken = Ingredient.objects.get(name='Chicken Breast')
        pasta = Ingredient.objects.get(name='Pasta')
        sauce = Ingredient.objects.get(name='Tomato Sauce')
        mozzarella = Ingredient.objects.get(name='Mozzarella')
        bacon = Ingredient.objects.get(name='Bacon')

        classic_burger = MenuItem.objects.get(title='Classic Burger')
        RecipeRequirement.objects.create(menu_item=classic_burger, ingredient=beef, quantity=0.25)
        RecipeRequirement.objects.create(menu_item=classic_burger, ingredient=lettuce, quantity=0.1)
        RecipeRequirement.objects.create(menu_item=classic_burger, ingredient=tomato, quantity=1)
        RecipeRequirement.objects.create(menu_item=classic_burger, ingredient=buns, quantity=1)

        cheeseburger = MenuItem.objects.get(title='Cheeseburger')
        RecipeRequirement.objects.create(menu_item=cheeseburger, ingredient=beef, quantity=0.25)
        RecipeRequirement.objects.create(menu_item=cheeseburger, ingredient=lettuce, quantity=0.1)
        RecipeRequirement.objects.create(menu_item=cheeseburger, ingredient=tomato, quantity=1)
        RecipeRequirement.objects.create(menu_item=cheeseburger, ingredient=buns, quantity=1)
        RecipeRequirement.objects.create(menu_item=cheeseburger, ingredient=cheese, quantity=0.1)

        bacon_cheeseburger = MenuItem.objects.get(title='Bacon Cheeseburger')
        RecipeRequirement.objects.create(menu_item=bacon_cheeseburger, ingredient=beef, quantity=0.25)
        RecipeRequirement.objects.create(menu_item=bacon_cheeseburger, ingredient=lettuce, quantity=0.1)
        RecipeRequirement.objects.create(menu_item=bacon_cheeseburger, ingredient=tomato, quantity=1)
        RecipeRequirement.objects.create(menu_item=bacon_cheeseburger, ingredient=buns, quantity=1)
        RecipeRequirement.objects.create(menu_item=bacon_cheeseburger, ingredient=cheese, quantity=0.1)
        RecipeRequirement.objects.create(menu_item=bacon_cheeseburger, ingredient=bacon, quantity=0.15)

        chicken_sandwich = MenuItem.objects.get(title='Chicken Sandwich')
        RecipeRequirement.objects.create(menu_item=chicken_sandwich, ingredient=chicken, quantity=0.3)
        RecipeRequirement.objects.create(menu_item=chicken_sandwich, ingredient=lettuce, quantity=0.1)
        RecipeRequirement.objects.create(menu_item=chicken_sandwich, ingredient=tomato, quantity=1)
        RecipeRequirement.objects.create(menu_item=chicken_sandwich, ingredient=buns, quantity=1)

        pasta_marinara = MenuItem.objects.get(title='Pasta Marinara')
        RecipeRequirement.objects.create(menu_item=pasta_marinara, ingredient=pasta, quantity=0.5)
        RecipeRequirement.objects.create(menu_item=pasta_marinara, ingredient=sauce, quantity=1)
        RecipeRequirement.objects.create(menu_item=pasta_marinara, ingredient=mozzarella, quantity=0.2)

        self.stdout.write(self.style.SUCCESS('Created recipe requirements'))
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
