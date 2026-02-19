from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/add/', views.IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('menu/', views.MenuItemListView.as_view(), name='menuitem_list'),
    path('menu/add/', views.MenuItemCreateView.as_view(), name='menuitem_create'),
    path('recipe/add/', views.RecipeRequirementCreateView.as_view(), name='recipe_create'),
    path('purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
    path('purchases/record/', views.record_purchase, name='purchase_record'),
]
