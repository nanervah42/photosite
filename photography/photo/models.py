from django.db import models

class Avatar(models.Model):
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Аватар', blank=False)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')




    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватары'