from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    role = models.CharField(max_length=30, choices=(('Admin', 'Admin'), ('Operator', 'Operator'), ('Driver', 'Driver')))

# class Order(models.Model):

class Operator(CustomUser):
    last_name = None
    email = None
    first_name = None
    is_staff = None
    is_superuser = None
    ish_vaqti = models.CharField(max_length=30)
    ismi = models.CharField(max_length=20)
    tel = models.CharField(max_length=40)

    def __str__(self):
        return self.ismi

class Client(models.Model):
    phone = models.CharField(max_length=30)
    total_bonus = models.PositiveIntegerField()

    def __str__(self):
        return self.phone

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    driver = models.ForeignKey("driver.Driver", on_delete=models.CASCADE, null=True)
    total_sum = models.PositiveIntegerField(default=0)
    baggage = models.BooleanField(default=False)
    for_women = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=(('Active', 'Active'), ('Boshlandi', 'Boshlandi'), ('Olindi', 'Olindi'), ('Tugadi', 'Tugadi'), ('Bekor_qilindi', 'Bekor_qilindi')))
    starting_point = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    grading_point = models.SmallIntegerField()
    date = models.DateField()
    time = models.TimeField()
    waiting_seconds = models.SmallIntegerField()

    def __str__(self):
        return self.client




