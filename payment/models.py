from django.db import models

from driver.models import Driver
from users.models import Operator

class Payment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=40, choices=(('Naxt', 'Naxt'), ('Karta', 'Karta')))
    date = models.DateField()
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount
