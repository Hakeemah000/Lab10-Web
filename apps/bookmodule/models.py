from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)  # عنوان الكتاب
    author = models.CharField(max_length=50)  # اسم المؤلف
    price = models.FloatField(default=0.0)  # سعر الكتاب
    edition = models.SmallIntegerField(default=1)  # الإصدار
