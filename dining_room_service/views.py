from django.http import HttpResponse
from django.template import loader

from .models import *

def create_show_func(aClass, order_field='pk', show_field='pk'):
	def show_func(request):
		template = loader.get_template('show.html')
		elements = aClass.objects.order_by(order_field)
		context = {
			'title': aClass._meta.verbose_name_plural,
			'header': aClass._meta.verbose_name_plural,
			'show_field': show_field,
			'elements': elements,
		}
		return HttpResponse(template.render(context, request))

	return show_func

show_funcs = {
	'user': create_show_func(User, 'username', 'username'),
	'product': create_show_func(Product, 'name', 'name'),
	'dish': create_show_func(Dish, 'name', 'name'),
	'diningroom': create_show_func(DiningRoom, 'name', 'name'),
	'comment': create_show_func(Comment, show_field='text'),
}