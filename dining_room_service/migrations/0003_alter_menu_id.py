# Generated by Django 4.1.4 on 2022-12-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dining_room_service', '0002_alter_comment_id_alter_diningroom_id_alter_dish_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
