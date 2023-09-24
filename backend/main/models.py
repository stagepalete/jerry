from django.db import models

# Create your models here.


class TestModel(models.Model):
    test1 = models.CharField(max_length=20)
    test2 = models.ForeignKey('main.TestModel2', on_delete=models.CASCADE)


class TestModel2(models.Model):
    test1 = models.CharField(max_length=5)
    test2 = models.DecimalField(max_digits=10, decimal_places=2)
    test3 = models.CharField(max_length=5)