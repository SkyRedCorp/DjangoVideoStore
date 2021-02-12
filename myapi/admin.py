from django.contrib import admin
from .models import USER, STORE, INVENTORY, MOVIE, RENTAL

admin.site.register(USER)
admin.site.register(STORE)
admin.site.register(MOVIE)
admin.site.register(RENTAL)
admin.site.register(INVENTORY)

# Register your models here.

