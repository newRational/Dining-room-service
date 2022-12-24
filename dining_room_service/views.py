from django.http import HttpResponse
from django.template import loader

from .models import *

# Функция, которая создает функции-контроллеры
def create_show_func(aClass, order_field='pk'):

	# Создаваемая функция-контроллер
	def show_func(request):

		# Путь к HTML шаблону страницы (templates/show.html, templates добавляет автоматически)
		template = loader.get_template('show.html')

		# Чем будет заполнен шаблон
		context = {
			'title': aClass._meta.verbose_name_plural,
			'header': aClass._meta.verbose_name_plural,
			'elements': aClass.objects.order_by(order_field),
		}
		return HttpResponse(template.render(context, request))

	return show_func


# Словарик с функциями контроллерами. 
# Этот словарик импортируется в dining_room_service/urls.py
show_funcs = {
	'user': create_show_func(User, 'username'),
	'product': create_show_func(Product, 'name'),
	'dish': create_show_func(Dish, 'name'),
	'diningroom': create_show_func(DiningRoom, 'name'),
	'comment': create_show_func(Comment),
}