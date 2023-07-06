from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Good(models.Model):
    name = models.CharField(max_length=255)          # наименование товара (раздела)
    article = models.CharField(max_length=20, blank=True) # артикул
    catalog_number = models.CharField(max_length=20, blank=True) # КАТАЛОЖНЫЙ НОМЕР
    description = models.TextField(blank=True)      # описание товара
    in_stock = models.DecimalField(default=0, db_index=True, decimal_places=2, max_digits=6)  # количество на складе
    cat1 = models.BigIntegerField(default=0, blank=False)   # номер раздела 1-ого уровня
    cat2 = models.BigIntegerField(default=0, blank=False)   # номер раздела 2-ого уровня
    cat3 = models.BigIntegerField(default=0, blank=False)   # номер раздела 3-его уровня
    is_good = models.BooleanField(default=True, blank=False)# True - товар, False - раздел
    price = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=12) # цена
    supplier = models.CharField(max_length=4, blank=True)   # поставщик

    def __str__(self):
        return self.name