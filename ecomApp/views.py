from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout


# index/home view
def index(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'index.html', context=context)


# about view
def about(request):
    return render(request, 'about.html')


# user login view
def login_user(request):

    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'login.html', context={'form': form})

    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)


# user signup/register view
def signup_user(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
        
        else:
            return render(request, 'signup.html', context={'form':form})


    form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context=context)

# user detail update view
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)

        form = UserUpdateForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()

            login(request, current_user)
            return redirect('update_user')
        return render(request, 'update_user.html', context={'form': form})

# user password change view
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if  request.method == 'POST':
            form = PasswordChangeForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                login(request, current_user)
                return redirect('update_user')
            else:
                return render(request, 'update_password.html', context={'form': form})
            
        else:
            form = PasswordChangeForm(current_user)
            return render(request, 'update_password.html', context={'form': form})

# user logout view
def logout_user(request):

    cart_data = request.session.get('cart')

    logout(request)

    if cart_data:
        request.session['cart'] = cart_data

    return redirect('home')


# single product display view
def productDisplay(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)


# product display filter by category
def category(request, cat):
    category = Category.objects.get(name=cat)
    products = Product.objects.filter(category=category)
    context = {'products': products, 'category': category}
    return render(request, 'category.html', context=context)
    