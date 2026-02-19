from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Sum, F
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm


@login_required
def home(request):
    """
    Home view showing dashboard with key metrics.
    """
    # Calculate total inventory cost
    ingredients = Ingredient.objects.all()
    total_inventory_cost = sum(
        ingredient.quantity * float(ingredient.price_per_unit) 
        for ingredient in ingredients
    )
    
    # Calculate total revenue
    purchases = Purchase.objects.all()
    total_revenue = sum(
        float(purchase.menu_item.price) 
        for purchase in purchases
    )
    
    # Calculate profit (revenue minus cost of inventory used)
    profit = total_revenue - total_inventory_cost
    
    context = {
        'total_inventory_cost': total_inventory_cost,
        'total_revenue': total_revenue,
        'profit': profit,
        'ingredient_count': ingredients.count(),
        'menu_item_count': MenuItem.objects.count(),
        'purchase_count': purchases.count(),
    }
    return render(request, 'inventory/home.html', context)


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredient_form.html'
    success_url = '/ingredients/'


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/ingredient_form.html'
    success_url = '/ingredients/'


class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'
    context_object_name = 'menu_items'


class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/menuitem_form.html'


class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'inventory/reciperequirement_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.all()
        return context


class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    context_object_name = 'purchases'
    ordering = ['-timestamp']


@login_required
def record_purchase(request):
    """
    Record a new purchase and update inventory.
    """
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            menu_item = form.cleaned_data['menu_item']
            
            # Check if all ingredients are available
            requirements = RecipeRequirement.objects.filter(menu_item=menu_item)
            
            # Validate inventory
            for requirement in requirements:
                if requirement.ingredient.quantity < requirement.quantity:
                    form.add_error(None, f"Not enough {requirement.ingredient.name} in inventory!")
                    return render(request, 'inventory/purchase_form.html', {'form': form})
            
            # Create purchase
            purchase = form.save()
            
            # Update inventory
            for requirement in requirements:
                requirement.ingredient.quantity -= requirement.quantity
                requirement.ingredient.save()
            
            return redirect('/purchases/')
    else:
        form = PurchaseForm()
    
    return render(request, 'inventory/purchase_form.html', {'form': form})
