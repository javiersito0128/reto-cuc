from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InventoryItem
from .forms import InventoryItemForm, LoginForm

def login_view(request):
    if request.session.get('is_logged_in'):
        return redirect('inventory_list')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username and password:  # Simulated login
                request.session['is_logged_in'] = True
                messages.success(request, 'Logged in successfully.')
                return redirect('inventory_list')
            else:
                messages.error(request, 'Please enter valid username and password.')
    else:
        form = LoginForm()
    return render(request, 'inventory/login.html', {'form': form})

def inventory_list(request):
    if not request.session.get('is_logged_in'):
        messages.warning(request, 'Please log in to access the inventory.')
        return redirect('login')
    items = InventoryItem.objects.all()
    form = InventoryItemForm()
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully.')
            return redirect('inventory_list')
        else:
            messages.error(request, 'Failed to add item. Please check the form.')
    return render(request, 'inventory/inventory_list.html', {'items': items, 'form': form})

def logout_view(request):
    if request.session.get('is_logged_in'):
        del request.session['is_logged_in']
        messages.success(request, 'Logged out successfully.')
    return redirect('login')