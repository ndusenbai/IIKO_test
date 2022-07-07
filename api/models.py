from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    job_start = models.DateField()
    job_money = models.IntegerField()
    job_title = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    type_title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.type_title