# Generated by Django 5.0.1 on 2024-01-31 11:40

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('ingredient', models.TextField(blank=True, null=True, verbose_name='Ingredient')),
                ('procedure', models.TextField(blank=True, null=True, verbose_name='Procedure')),
                ('cocking_time', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cocking')),
                ('image', models.ImageField(upload_to='pic', verbose_name='Image')),
                ('video', models.FileField(upload_to='video', verbose_name='Video')),
                ('review', models.TextField(default=1, verbose_name='Review')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='RecipeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rate')),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Recipe Rate',
                'verbose_name_plural': 'Recipes Rate',
                'unique_together': {('user_id', 'dish_id')},
            },
        ),
        migrations.CreateModel(
            name='SavedDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Saved Dish',
                'verbose_name_plural': 'Saved Dishes',
                'unique_together': {('user_id', 'dish_id')},
            },
        ),
    ]
