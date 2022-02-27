from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


# Home Page (home.html)
def home(request):
    # Collect all houses for introduction on Home page
    context = {}

    return render(request,
                  'myappocalypse/home.html',
                  context=context)


def login(request):
    if request.method == "POST":
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            context['successMsg'] = 'Successful login'
            return render(request, 'myappocalypse/login.html', context=context)
        else:
            context['errorMsg'] = 'Invalid login'
            return render(request, 'myappocalypse/login.html', context=context)
    else:
        return render(request, 'myappocalypse/login.html')