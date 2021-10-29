# Generated by Django 3.2.8 on 2021-10-29 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_instagramsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='WorksPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фотографии работ')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='photo.workscategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Фотографии работ',
                'verbose_name_plural': 'Фотографии работ',
            },
        ),
    ]
