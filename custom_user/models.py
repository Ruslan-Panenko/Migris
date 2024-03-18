from django.db import models


class CustomUser(models.Model):
    migris = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField()
    passport = models.CharField(max_length=255)
    expired_date = models.DateField()
    phone_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} -- {self.surname}'
