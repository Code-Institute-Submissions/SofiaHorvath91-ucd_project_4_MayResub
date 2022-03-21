from django.urls import path
from .views import (
    home,
    signin,
    signout,
    signup,
    packmybag,
    add_items,
    mybag_details,
    blog,
    profile,
    whyabag,
)

urlpatterns = [
    path('', home, name="home"),
    path('whyabag/', whyabag, name='whyabag'),
    path('signup/', signup, name='signup'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('packmybag/', packmybag, name='packmybag'),
    path('mybag_add_items/<int:id>', add_items, name='mybag_add_items'),
    path('mybag_details/<int:id>', mybag_details, name='mybag_details'),
    path('blog/', blog, name='blog'),
    path('profile/', profile, name='profile'),
]
