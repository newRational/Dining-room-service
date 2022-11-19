# Generated by Django 4.1.3 on 2022-11-13 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('name', models.CharField(max_length=150, verbose_name='Столовая')),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('price', models.PositiveSmallIntegerField(help_text='указывать сумму в рублях', verbose_name='Цена')),
                ('weight', models.PositiveSmallIntegerField(help_text='указывать массу в граммах', verbose_name='Вес')),
                ('calories', models.PositiveSmallIntegerField(help_text='указывать в ккал', verbose_name='Калорийность')),
                ('numberOfRated', models.PositiveSmallIntegerField(verbose_name='Количество пользователей оценивших блюдо')),
                ('overallRating', models.PositiveSmallIntegerField(verbose_name='Сумма оценок пользователей')),
                ('recommendation', models.BooleanField(default=False, verbose_name='Рекомендация повара')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='Продукт')),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Никнейм')),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('status', models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher'), ('COOK', 'Cook'), ('ADMIN', 'Admin')], default='STUDENT', max_length=7)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('dishes', models.ManyToManyField(to='dining_room_service.dish', verbose_name='блюда')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.AddField(
            model_name='dish',
            name='products',
            field=models.ManyToManyField(to='dining_room_service.product', verbose_name='ингредиенты'),
        ),
        migrations.CreateModel(
            name='DiningRoom',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='Столовая')),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('timetable', models.DateTimeField(verbose_name='Расписание')),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSE', 'Close')], default='OPEN', max_length=5)),
                ('dayMenu', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='day_menu', to='dining_room_service.menu', verbose_name='меню на день')),
                ('extendedMenu', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extended_menu', to='dining_room_service.menu', verbose_name='расширенное меню')),
            ],
            options={
                'verbose_name': 'Столовая',
                'verbose_name_plural': 'Столовые',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField(max_length=5000, verbose_name='Текст')),
                ('dayTime', models.DateTimeField(verbose_name='Дата и время')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dining_room_service.user', verbose_name='автор')),
                ('dish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dining_room_service.dish', verbose_name='блюдо')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
