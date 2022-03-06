from django.contrib import admin
from .models import Item, Bag, Climate, Landform, Environment

# Register your models here.
admin.site.register(Item)
admin.site.register(Bag)
admin.site.register(Climate)
admin.site.register(Landform)
admin.site.register(Environment)