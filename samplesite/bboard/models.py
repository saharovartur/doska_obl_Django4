from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')


    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')


    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявления'
        ordering = ['-published']

