from django.contrib import admin
from . models import User, Product, Dish, Menu, DiningRoom, Comment, Timetable


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Dish)
admin.site.register(Menu)
admin.site.register(DiningRoom)
admin.site.register(Comment)
admin.site.register(Timetable)