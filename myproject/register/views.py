from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main1.models import Position, Order, Artist  # Import the necessary models
from django.db.models import F, ExpressionWrapper, DecimalField
from django.db.models.functions import Coalesce

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            form.save()

            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})



def user_login(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page or wherever you want
                return redirect("/")
            else:
                # Authentication failed, display an error message
                form.add_error(None, "Invalid credentials")
    else:
        form = CustomLoginForm()

    return render(request, "registration/login.html", {"form": form})



def user_logout(request):
    logout(request)
    
    # Redirect to login page
    return redirect("login")

@login_required
def profile(request):
    user = request.user
    
    # Get user's positions
    positions = Position.objects.filter(user=user).select_related('artist')
    portfolio = []
    total_portfolio_value = 0
    
    for position in positions:
        current_price = position.artist.current_price()  # Implement this method in your Artist model
        total_value = position.shares * current_price
        gain_loss = total_value - (position.shares * position.average_price)
        gain_loss_percentage = (gain_loss / (position.shares * position.average_price)) * 100 if position.average_price else 0
        
        portfolio.append({
            'artist': position.artist.name,
            'shares': position.shares,
            'purchase_price': position.average_price,
            'current_price': current_price,
            'total_value': total_value,
            'gain_loss': gain_loss,
            'gain_loss_percentage': gain_loss_percentage,
        })
        
        total_portfolio_value += total_value
    
    # Get recent orders
    recent_orders = Order.objects.filter(user=user).order_by('-date')[:10]  # Get last 10 orders
    
    # Calculate total value for each order
    recent_orders = recent_orders.annotate(
        total_value=ExpressionWrapper(
            F('num_shares') * F('price'),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )
    )
    
    context = {
        'user': user,
        'portfolio': portfolio,
        'total_portfolio_value': total_portfolio_value,
        'recent_orders': recent_orders,
    }
    
    return render(request, 'registration/profile.html', context)
