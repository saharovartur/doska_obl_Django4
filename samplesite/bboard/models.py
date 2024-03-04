from django.db import models


class Rubric(models.Model):
    """Модель 'Рубрики' хранит один атрибут с полем названия рубрики"""
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        """Настроечный класс для админки."""
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

class Bb(models.Model):
    """Модель 'Объявления'  хранит атрибуты с столбцами таблицы"""
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Категория')
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')


    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявления'
        ordering = ['-published']

