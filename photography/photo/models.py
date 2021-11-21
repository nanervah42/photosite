from django.db import models
from django_resized import ResizedImageField

class Avatar(models.Model):
    # photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Аватар', blank=False)
    photo = ResizedImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Аватар', blank=False)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватары'

class Carousel(models.Model):
    # photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Карусель', blank=False)
    photo = ResizedImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Карусель', blank=False)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусель'


class InstagramSection(models.Model):
    # photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Инстаграм линия', blank=False)
    photo = ResizedImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Инстаграм линия', blank=False)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Инстаграм линия'
        verbose_name_plural = 'Инстаграм линия'


class WorksCategory(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Фотографии работ (категории)')

    class Meta:
        verbose_name = 'Фотографии работ (категории)'
        verbose_name_plural = 'Фотографии работ (категории)'

    def __str__(self):
        return self.title


class WorksPhotos(models.Model):
    # photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фотографии работ', blank=False)
    photo = ResizedImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фотографии работ', blank=False)
    category = models.ForeignKey('WorksCategory', on_delete=models.PROTECT, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Фотографии работ'
        verbose_name_plural = 'Фотографии работ'
        ordering = ['-pk']