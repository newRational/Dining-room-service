from django.db import models


class User(models.Model):
    """Пользователь"""
    username = models.CharField("Никнейм", max_length=100, unique=True)
    #id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    firstname = models.CharField("Имя", max_length=100)
    lastname = models.CharField("Фамилия", max_length=100)
    password = models.CharField("Пароль", max_length=100)
    status = models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher'), ('COOK', 'Cook'),
                                       ('ADMIN', 'Admin')], default='STUDENT', max_length=7)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Product(models.Model):
    """Продукт"""
    name = models.CharField("Продукт", max_length=100)
    #id = models.PositiveSmallIntegerField(unique=True, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Dish(models.Model):
    """Блюдо"""
    name = models.CharField("Столовая", max_length=150)
    #id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    price = models.PositiveSmallIntegerField("Цена", help_text="указывать сумму в рублях")
    weight = models.PositiveSmallIntegerField("Вес", help_text="указывать массу в граммах")
    calories = models.PositiveSmallIntegerField("Калорийность", help_text="указывать в ккал")
    products = models.ManyToManyField(Product, verbose_name="ингредиенты")
    numberOfRated = models.PositiveSmallIntegerField("Количество пользователей оценивших блюдо")
    overallRating = models.PositiveSmallIntegerField("Сумма оценок пользователей")
    recommendation = models.BooleanField("Рекомендация повара", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Menu(models.Model):
    """Меню"""
    #id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    dishes = models.ManyToManyField(Dish, verbose_name="блюда")

    """def __str__(self):
        return self.id"""

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class DiningRoom(models.Model):
    """Столовая"""
    name = models.CharField("Столовая", max_length=100)
    #id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    # пока не нашёл хороший способ хранить расписание
    timetable = models.DateTimeField("Расписание")
    dayMenu = models.OneToOneField(Menu, verbose_name="меню на день", related_name="day_menu",
                                   on_delete=models.SET_NULL, null=True)
    extendedMenu = models.OneToOneField(Menu, verbose_name="расширенное меню", related_name="extended_menu",
                                        on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=[('OPEN', 'Open'), ('CLOSE', 'Close')], default='OPEN', max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Столовая"
        verbose_name_plural = "Столовые"


class Comment(models.Model):
    """Комментарий"""
    #id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    text = models.TextField("Текст", max_length=5000)
    dish = models.ForeignKey(Dish, verbose_name="блюдо", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, verbose_name="автор", on_delete=models.SET_NULL, null=True)
    dayTime = models.DateTimeField("Дата и время")

    """def __str__(self):
        return self.id"""

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
