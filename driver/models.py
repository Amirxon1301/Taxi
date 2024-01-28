from django.db import models
from users.models import CustomUser

class CarCategory(models.Model):
    minimum = models.IntegerField()
    waiting_cost = models.IntegerField()
    bonus_percent = models.IntegerField()
    baggage_cost = models.IntegerField()
    type = models.CharField(max_length=40)
    sum_per_km = models.IntegerField()

    def __str__(self):
        return self.type


class Driver(CustomUser):
    last_name = None
    email = None
    first_name = None
    is_staff = None
    is_superuser = None
    fullname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    car_type = models.CharField(max_length=30)
    car_number = models.CharField(max_length=40)
    sms_code = models.CharField(max_length=40)
    confirmed = models.BooleanField(default=False)
    balance = models.PositiveIntegerField()
    gender = models.CharField(max_length=30, choices=(('Erkak', 'Erkak'), ('Ayol', 'Ayol')))
    has_baggage = models.BooleanField(default=False)
    created_at = models.DateField()
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    photo = models.FileField()
    birth_date = models.DateField()

    def __str__(self):
        return self.fullname

