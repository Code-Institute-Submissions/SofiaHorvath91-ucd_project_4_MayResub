from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Item, Bag, Climate, Landform, Environment

User = get_user_model()


# Home Page (home.html)
def home(request):
    # Collect all houses for introduction on Home page
    context = {}
    return render(request, 'myappocalypse/home.html', context=context)


def signin(request):
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


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'myappocalypse/login.html')
    else:
        return redirect('myappocalypse/login.html')


def signup(request):
    if request.method == "POST":
        context = {}
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            username = request.POST['username']
            email = request.POST['email']

            try:
                user1 = User.objects.get(username=username)
                context['errorMsg'] = 'Username is already in system'
                return render(request, 'myappocalypse/signup.html', context=context)
            except User.DoesNotExist:
                try:
                    user2 = User.objects.get(email=email)
                    context['errorMsg'] = 'Email is already in system'
                    return render(request, 'myappocalypse/signup.html', context=context)
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    return redirect('home')
        else:
            context['errorMsg'] = 'Passwords must match'
            return render(request, 'myappocalypse/signup.html', context=context)
    else:
        return render(request, 'myappocalypse/signup.html')


def packmybag(request):
    context = {}
    if request.method == "POST":
        user = request.user
        name = request.POST['bagname']
        userweight = request.POST['userweight']
        bagweight = request.POST['bagweight']
        have_child = request.POST.get('have_child', False)
        have_elder = request.POST.get('have_elder', False)
        have_pet = request.POST.get('have_pet', False)
        climate = request.POST['climate']
        landform = request.POST['landform']
        environment = request.POST['environment']
        human_infra = request.POST['human_infra']
        drinking_water = request.POST['drinking_water']
        comestible_food = request.POST['comestible_food']

        if climate == 'default' or landform == 'default' or environment == 'default' \
                or human_infra == 'default' or drinking_water == 'default' or comestible_food == 'default':
            context['errorMsg'] = 'Choose all types, please'
            return render(request, 'myappocalypse/packmybag.html', context=context)
        else:
            bag = Bag.objects.create(user=user, name=name, weight_bag=bagweight, weight_user=userweight,
                                     climate=Climate.objects.filter(name=climate).first(),
                                     landform=Landform.objects.filter(name=landform).first(),
                                     environment=Environment.objects.filter(name=environment).first(),
                                     with_child=have_child, with_elder=have_elder, with_pet=have_pet,
                                     available_infrastructure=human_infra,
                                     available_water=drinking_water, available_food=comestible_food)
            bag.save()
            return redirect('mybag_add_items', id=bag.id)

    return render(request, 'myappocalypse/packmybag.html', context=context)


def add_items(request, id):
    context = {}

    items = Item.objects.all()
    context['items'] = items
    return render(request, 'myappocalypse/mybag_add_items.html', context=context)

