# Generated by Django 5.0.1 on 2024-01-25 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
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
                ('rate', models.PositiveIntegerField(default=1, verbose_name='Rate')),
                ('review', models.TextField(default=1, verbose_name='Review')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
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
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pic', verbose_name='Image')),
                ('file', models.FileField(upload_to='video', verbose_name='File')),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Medias',
            },
        ),
        migrations.CreateModel(
            name='SavedDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name': 'Saved Dish',
                'verbose_name_plural': 'Saved Dishes',
            },
        ),
    ]
