from django.contrib import admin
# from models import Menu # menu is not in the same directory
from .models import Menu # the dot is used to denote that  menu is in the same directory
from .models import Logger # the dot is used to denote that  menu is in the same directory
from .models import Reservation # the dot is used to denote that Reservation is in the same directory


# Register your models here.
admin.site.register(Menu)
admin.site.register(Logger)
admin.site.register(Reservation)
