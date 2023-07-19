
from django.contrib import admin
from .models import details,Person,City,Country

admin.site.register(Country)
admin.site.register(City)
admin.site.register(details)