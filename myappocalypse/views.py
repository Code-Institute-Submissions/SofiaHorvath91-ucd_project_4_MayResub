from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from itertools import chain
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.decorators import login_required

from .models import Item, Bag, Climate, Landform, Environment, ItemSerializer, Feedback, Recommendation
User = get_user_model()


# Home Page (home.html)
def home(request):
    return render(request, 'myappocalypse/home.html')


# Why A Bag Page (whyabag.html)
# => Page Aim : Description / justification of application
def whyabag(request):
    return render(request, 'myappocalypse/whyabag.html')


# Login Page (login.html)
# => Page Aim :
# Allow registered users to login
# via standard form / social login (Facebook, Twitter, Google)
def signin(request):
    context = {}

    # Get username and password from user
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if username-password exists, and allow login if so
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


# Sign Up Page (signup.html)
# => Page Aim :
# Allow not registered users to sign up via
# standard form / social login (Facebook, Twitter, Google)
def signup(request):
    context = {}

    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 == password2:
            username = request.POST['username']
            email = request.POST['email']

            # Check if username already exists
            try:
                user1 = User.objects.get(username=username)
                context['errorMsg'] = 'Username is already in system'
                return render(request, 'myappocalypse/signup.html', context=context)
            except User.DoesNotExist:
                # If username is unique, check if email already exists
                try:
                    user2 = User.objects.get(email=email)
                    context['errorMsg'] = 'Email is already in system'
                    return render(request, 'myappocalypse/signup.html', context=context)
                except User.DoesNotExist:
                    # If email and username are unique, create user
                    user = User.objects.create_user(username=username,
                                                    email=email,
                                                    password=password1)
                    context['successMsg'] = "Thank you for signing up!"
                    return redirect('home')
        else:
            context['errorMsg'] = 'Passwords must match'
            return render(request, 'myappocalypse/signup.html', context=context)
    else:
        return render(request, 'myappocalypse/signup.html')


# Logout Page (logout.html)
# => Page Aim :
# Allow already logged in users to logout
@login_required
def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('myappocalypse/logout.html')


# Pack A Bag Page (packmybag.html)
# => Page Aim :
# Allow logged in users to create a new bag
# in which one can pack items after
@login_required
def packmybag(request):
    context = {}

    if request.method == "POST":
        # Get bag details from user form
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

        # Check if climate / landform / environment picklists are selected
        # (value true or false, not default)
        if climate == 'default' or landform == 'default' or environment == 'default' \
                or human_infra == 'default' or drinking_water == 'default' or comestible_food == 'default':
            context['errorMsg'] = 'Choose all types, please'
            return render(request, 'myappocalypse/packmybag.html', context=context)
        # Check if climate Dry was paired with matching Desert environment
        if (climate == 'Dry' and landform != 'Ocean') and environment != 'Desert':
            context['errorMsg'] = 'For Dry climate, please choose Desert environment'
            return render(request, 'myappocalypse/packmybag.html', context=context)
        # Check if climate Polar was paired with matching Tundra environment
        if (climate == 'Polar' and landform != 'Ocean') and environment != 'Tundra':
            context['errorMsg'] = 'For Polar climate, please choose Tundra environment'
            return render(request, 'myappocalypse/packmybag.html', context=context)
        # Check if landform Ocean was paired with matching Marine environment
        if landform == 'Ocean' and (environment != 'Marine' or climate == 'Dry'):
            context['errorMsg'] = 'For Ocean landform, please choose Marine environment'
            return render(request, 'myappocalypse/packmybag.html', context=context)
        else:
            # If all bag details are filled out appropriately, create bag,
            bag = Bag.objects.create(user=user,
                                     name=name,
                                     weight_bag=bagweight,
                                     weight_user=userweight,
                                     climate=Climate.objects.filter(name=climate).first(),
                                     landform=Landform.objects.filter(name=landform).first(),
                                     environment=Environment.objects.filter(name=environment).first(),
                                     with_child=have_child,
                                     with_elder=have_elder,
                                     with_pet=have_pet,
                                     available_infrastructure=human_infra,
                                     available_water=drinking_water,
                                     available_food=comestible_food)
            bag.save()
            # Once bag is created, redirect user to page to add items to bag
            return redirect('mybag_add_items', id=bag.id)

    return render(request, 'myappocalypse/packmybag.html', context=context)


# Add Items Page (mybag_add_items/<bag ID>.html)
# => Page Aim :
# Allow logged in users to add items recommended
# based on bag details to newly created or existing bag
@login_required
def add_items(request, id):
    context = {}

    # Get newly created bag
    bag = Bag.objects.filter(id=id).first()
    context['bag'] = bag

    # Pass existing items' list and actual bag weight for use in case of edit, not creation
    if bag.weight_bag_actual is not None:
        context['existing_items'] = bag.items.all()
        context['actual_weight'] = round(bag.weight_bag_actual)

    # Pass all items to Javascript via json
    all_items = Item.objects.all()
    serializer = ItemSerializer(all_items, many=True)
    data = JSONRenderer().render(serializer.data)
    context['items_json'] = data.decode()

    # Set items recommended based on bag details
    items_by_locale = Item.objects.filter(climate__in=[bag.climate],
                                          landform__in=[bag.landform],
                                          environment__in=[bag.environment])
    items_all_company_condition = items_by_locale.filter(with_child=None,
                                                         with_elder=None,
                                                         with_pet=None,
                                                         available_infrastructure=None,
                                                         available_water=None,
                                                         available_food=None)
    context['basic_items'] = items_all_company_condition
    context['items_user_company'] = get_items_by_company(items_by_locale)
    context['items_user_condition'] = get_items_by_conditions(items_by_locale, bag)
    context['choices'] = get_choices_array()

    # Add selected items to bag
    if request.method == "POST":
        selected_items = request.POST.getlist('item_checkbox')

        # Check if any item selected
        if len(selected_items) > 0:
            # Get items from database based on user input of selected items
            # and add them to bag 'items' field as list
            bagweight = request.POST['additems_new_bag_weight']
            items_to_create = []
            for i in all_items:
                if i.name in selected_items:
                    items_to_create.append(i)
            bag.items.set(items_to_create)
            # Update actual weight of bag based on the total weight of selected items
            bag.weight_bag_actual = bagweight
            bag.save()
            return redirect('mybag_details', id=bag.id)
        else:
            context['errorMsg'] = 'Please add at least 1 item to the bag'
            return render(request, 'myappocalypse/mybag_add_items.html', context=context)

    return render(request, 'myappocalypse/mybag_add_items.html', context=context)


# Detail of a Bag Page (mybag_details/<bag ID>.html)
# => Page Aim :
# Allow logged in users to checks details of an already created bag
@login_required
def mybag_details(request, id):
    context = {}

    # Get a given bag based on ID
    bag = Bag.objects.filter(id=id).first()
    context['bag'] = bag

    # Pass items of bag to Javascript via json
    serializer = ItemSerializer(bag.items, many=True)
    data = JSONRenderer().render(serializer.data)
    context['items_json'] = data.decode()

    # Get an sort bag items to show them in sections / category on UI
    items_all_company_condition = bag.items.filter(with_child=None,
                                                   with_elder=None,
                                                   with_pet=None,
                                                   available_infrastructure=None,
                                                   available_water=None,
                                                   available_food=None)
    context['basic_items'] = items_all_company_condition
    context['items_user_company'] = get_items_by_company(bag.items)
    context['items_user_condition'] = get_items_by_conditions(bag.items, bag)
    context['choices'] = get_choices_array()

    # Quick actions from page
    if request.method == "POST":
        # Delete a bag
        if request.POST.get('thisbag-to-delete'):
            bag = Bag.objects.filter(id=request.POST['thisbag-to-delete']).first()
            bag.delete()
            return redirect('profile')

    return render(request, 'myappocalypse/mybag_details.html', context=context)


# Blog Page (blog.html)
# => Page Aim :
# Allow logged in users to leave star-based feedback & comment about the site,
# recommend an item and consult existing feedbacks
@login_required
def blog(request):
    context = {}

    # Pass all existing feedbacks to show them as list
    context['feedbacks'] = Feedback.objects.all()

    # Get star-based rating and/or text-based comment from user
    # (Click on Send Feedback button)
    if request.method == "POST" and request.POST.get('feedback') or request.POST.get('rating'):
        rating = request.POST.get('rating').split('_')[0]
        rating_desc = request.POST.get('rating').split('_')[1]
        content = request.POST['feedback']

        # Create feedback only if either star-based rating,
        # either text-based comment, either both were provided
        if content or (rating != '0'):
            user = request.user
            feedback = Feedback.objects.create(rating_point=rating,
                                               rating_description=rating_desc,
                                               content=content,
                                               user=user)
            feedback.save()
            return redirect('blog')
        else:
            context['errorMsg'] = 'Please share your feedback or rating!'
            return render(request, 'myappocalypse/blog.html', context=context)

    # Allow feedback owner or admin user (superuser) to delete feedback from list
    # (Click on Delete button of a feedback)
    if request.method == "POST" and request.POST.get('feedback-to-delete'):
        feedback = Feedback.objects.filter(id=request.POST['feedback-to-delete']).first()
        feedback.delete()
        return redirect('blog')

    # Get recommended item from user (Click on Recommend Item button)
    if request.method == "POST" and request.POST.get('item_name'):
        user = request.user
        name = request.POST['item_name']
        weight = request.POST['weight']
        category = request.POST['category']
        usefulness = request.POST['usefulness']
        external = request.POST['external']
        justification = request.POST['justification']

        # Check if category / external picklists are selected
        # (value true or false, not default)
        if category == 'default' or external == 'default':
            context['errorMsg'] = 'Set value for all fields, please'
            return render(request, 'myappocalypse/blog.html', context=context)
        else:
            # If all recommendation details are filled out appropriately,
            # create recommendation for admin approval
            recommendation = Recommendation.objects.create(user=user,
                                                           name=name,
                                                           weight=weight,
                                                           category=category,
                                                           justification=justification,
                                                           usefulness=usefulness,
                                                           external=external,
                                                           status='Pending')
            recommendation.save()
        return render(request, 'myappocalypse/blog.html', context=context)

    return render(request, 'myappocalypse/blog.html', context=context)


# Profile Page (profile.html)
# => Page Aim :
# Allow logged in users to consult their bags,
# feedbacks and recommendations in one place
@login_required
def profile(request):
    context = {}
    context['user'] = request.user

    # Select bags created by current user (so deleting bags only allowed for owner)
    context['bags'] = Bag.objects.filter(user=request.user)

    # Delete object records
    if request.method == "POST":
        # Delete a feedback, allowed for feedback owner / request user and admin / superuser
        if request.POST.get('myfeedback-to-delete'):
            feedback = Feedback.objects.filter(id=request.POST['myfeedback-to-delete']).first()
            feedback.delete()
            return redirect('profile')
        # Delete a bag, allowed only for bag owner
        if request.POST.get('mybag-to-delete'):
            bag = Bag.objects.filter(id=request.POST['mybag-to-delete']).first()
            bag.delete()
            return redirect('profile')
        # Delete a recommendation, allowed only for recommendation owner
        if request.POST.get('myrecommendations-to-delete'):
            recommendation = Recommendation.objects.filter(id=request.POST['myrecommendations-to-delete']).first()
            recommendation.delete()
            return redirect('profile')
        # Approve recommendation, allowed only for admin / superuser
        if request.POST.get('recommendations-to-approve') and request.user.is_superuser:
            recommendation = Recommendation.objects.filter(id=request.POST['recommendations-to-approve']).first()
            recommendation.status = 'Approved'
            recommendation.save()
            return redirect('profile')
        # Reject recommendation, allowed only for admin / superuser
        if request.POST.get('recommendations-to-reject') and request.user.is_superuser:
            recommendation = Recommendation.objects.filter(id=request.POST['recommendations-to-approve']).first()
            recommendation.status = 'Rejected'
            recommendation.save()
            return redirect('profile')

    # Select feedbacks and recommendations
    if request.user.is_superuser:
        # If user is admin (superuser), show all feedbacks
        # and all recommendations with Pending status, regardless of owner
        context['feedbacks'] = Feedback.objects.all()
        context['recommendations'] = Recommendation.objects.filter(status='Pending')
        return render(request, 'myappocalypse/profile.html', context=context)
    else:
        # If user is standard user, show own feedbacks and recommendations
        context['feedbacks'] = Feedback.objects.filter(user=request.user)
        context['recommendations'] = Recommendation.objects.filter(user=request.user)
        return render(request, 'myappocalypse/profile.html', context=context)


# Helper classes


# Get text value of Category choices field of Item object / model
def get_choices_array():
    choices = Item._meta.get_field('category').choices
    category_choices = []
    for c in choices:
        if '_' in c[0]:
            category_choices.append(c[0].replace('_', ' & '))
        else:
            category_choices.append(c[0])
    return category_choices


# Get all items specific to special company
def get_items_by_company(items):
    items_with_child = items.filter(with_child=True)
    items_with_elder = items.filter(with_elder=True)
    items_with_pet = items.filter(with_pet=True)
    items_user_company = list(chain(items_with_child,
                                    items_with_elder,
                                    items_with_pet))
    return items_user_company


# Get items specific to special conditions precised for a bag
def get_items_by_conditions(items, bag):
    items_user_humaninfra = items.filter(available_infrastructure=bag.available_infrastructure)
    items_user_water = items.filter(available_water=bag.available_water)
    items_user_food = items.filter(available_food=bag.available_food)
    items_user_condition = list(chain(items_user_humaninfra,
                                      items_user_water,
                                      items_user_food))
    return items_user_condition
