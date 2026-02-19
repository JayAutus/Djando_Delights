from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase


class RecipeRequirementInline(admin.TabularInline):
    model = RecipeRequirement
    extra = 1


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [RecipeRequirementInline]
    list_display = ['title', 'price']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit', 'price_per_unit']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'timestamp']
    readonly_fields = ['timestamp']


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase, PurchaseAdmin)
