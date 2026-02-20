from decimal import Decimal
from typing import cast

from django.db import models


class Ingredient(models.Model):
    """
    Represents an ingredient in the restaurant's inventory.
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0.0, help_text="Available quantity in inventory")  # type: ignore[arg-type]
    unit = models.CharField(max_length=50, default="unit", help_text="Unit of measurement (e.g., lbs, oz, units)")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit")

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit} @ ${self.price_per_unit}/{self.unit}"

    def get_total_value(self):
        """
        Calculate the total value of this ingredient in inventory.
        """
        return float(cast(float, self.quantity)) * float(cast(Decimal, self.price_per_unit))


class MenuItem(models.Model):
    """
    Represents an item on the restaurant's menu.
    """
    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - ${self.price}"

    def available(self):
        """
        Check if the menu item can be made with current inventory.
        """
        return all(
            ingredient.enough()
            for ingredient in self.reciperequirement_set.all()  # type: ignore[attr-defined]
        )

    def get_absolute_url(self):
        return "/menu/"


class RecipeRequirement(models.Model):
    """
    Represents the amount of an ingredient required for a menu item.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Quantity of ingredient required")

    def __str__(self):
        menu_item = cast("MenuItem", self.menu_item)
        ingredient = cast("Ingredient", self.ingredient)
        return f"{menu_item.title} requires {self.quantity} {ingredient.unit} of {ingredient.name}"

    def enough(self):
        """
        Check if there is enough of this ingredient in inventory.
        """
        ingredient = cast("Ingredient", self.ingredient)
        return ingredient.quantity >= self.quantity


class Purchase(models.Model):
    """
    Represents a customer purchase of a menu item.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        menu_item = cast("MenuItem", self.menu_item)
        return f"{menu_item.title} purchased at {self.timestamp}"

    def get_absolute_url(self):
        return "/purchases/"
