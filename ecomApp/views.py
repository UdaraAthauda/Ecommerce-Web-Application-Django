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

# user logout view
def logout_user(request):
    logout(request)
    return redirect('home')