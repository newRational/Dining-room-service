from django.urls import path

from .views import show_funcs

# Из словарика show_funcs достаются нужные
# функции-контроллеры
urlpatterns = [
	path('users', show_funcs['user']),
	path('products', show_funcs['product']),
	path('dishes', show_funcs['dish']),
	path('diningrooms', show_funcs['diningroom']),
	path('comments', show_funcs['comment']),
]