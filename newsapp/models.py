from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)

"""
Person.objects.create(first_name='ani', last_name='amir')
Person.objects.create(first_name='john', last_name='john')
Person.objects.get(first_name='ani')
Person.objects.filter(first_name='ani')
Person.objects.all()
"""


class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)