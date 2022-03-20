from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from itertools import chain

from django.core import serializers
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.decorators import login_required

from .models import Item, Bag, Climate, Landform, Environment, ItemSerializer

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
        if climate == 'Dry' and environment != 'Desert':
            context['errorMsg'] = 'For Dry climate, please choose Desert environment'
            return render(request, 'myappocalypse/packmybag.html', context=context)
        if climate == 'Polar' and environment != 'Tundra':
            context['errorMsg'] = 'For Polar climate, please choose Tundra environment'
            return render(request, 'myappocalypse/packmybag.html', context=context)
        if landform == 'Ocean' and environment != 'Marine':
            context['errorMsg'] = 'For Ocean landform, please choose Marine environment'
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

    bag = Bag.objects.filter(id=id).first()
    context['bag'] = bag

    all_items = Item.objects.all()
    serializer = ItemSerializer(all_items, many=True)
    data = JSONRenderer().render(serializer.data)
    context['items_json'] = data.decode()

    items_by_locale = Item.objects.filter(climate__in=[bag.climate], landform__in=[bag.landform],
                                          environment__in=[bag.environment])
    items_all_company_condition = items_by_locale.filter(with_child=None, with_elder=None, with_pet=None,
                                                         available_infrastructure=None, available_water=None,
                                                         available_food=None)
    context['basic_items'] = items_all_company_condition
    context['items_user_company'] = get_items_by_company(items_by_locale)
    context['items_user_condition'] = get_items_by_conditions(items_by_locale, bag)
    context['choices'] = get_choices_array()

    if request.method == "POST":
        selected_items = request.POST.getlist('item_checkbox')
        bagweight = request.POST['additems_new_bag_weight']
        items_to_create = []
        for i in all_items:
            if i.name in selected_items:
                items_to_create.append(i)
        bag.items.set(items_to_create)
        bag.weight_bag_actual = bagweight
        bag.save()
        return redirect('mybag_details', id=bag.id)

    return render(request, 'myappocalypse/mybag_add_items.html', context=context)


def mybag_details(request, id):
    context = {}

    bag = Bag.objects.filter(id=id).first()
    context['bag'] = bag

    serializer = ItemSerializer(bag.items, many=True)
    data = JSONRenderer().render(serializer.data)
    context['items_json'] = data.decode()

    items_all_company_condition = bag.items.filter(with_child=None, with_elder=None, with_pet=None,
                                                   available_infrastructure=None, available_water=None,
                                                   available_food=None)
    context['basic_items'] = items_all_company_condition
    context['items_user_company'] = get_items_by_company(bag.items)
    context['items_user_condition'] = get_items_by_conditions(bag.items, bag)
    context['choices'] = get_choices_array()

    return render(request, 'myappocalypse/mybag_details.html', context=context)


# Helper classes


def get_choices_array():
    choices = Item._meta.get_field('category').choices
    category_choices = []
    for c in choices:
        if '_' in c[0]:
            category_choices.append(c[0].replace('_', ' & '))
        else:
            category_choices.append(c[0])
    return category_choices


def get_items_by_company(items):
    items_with_child = items.filter(with_child=True)
    items_with_elder = items.filter(with_elder=True)
    items_with_pet = items.filter(with_pet=True)
    items_user_company = list(chain(items_with_child, items_with_elder, items_with_pet))
    return items_user_company


def get_items_by_conditions(items, bag):
    items_user_humaninfra = items.filter(available_infrastructure=bag.available_infrastructure)
    items_user_water = items.filter(available_water=bag.available_water)
    items_user_food = items.filter(available_food=bag.available_food)
    items_user_condition = list(chain(items_user_humaninfra, items_user_water, items_user_food))
    return items_user_condition


