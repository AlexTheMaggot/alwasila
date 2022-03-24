from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    img = models.ImageField(upload_to='product_img/', verbose_name='Изображение (370 x 479 px)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
