from django.db import models


# Create your models here.


class Balance(models.Model):
    balance_name = models.CharField(max_length=200)
    pocket_value = models.FloatField()
    pocket_label = models.CharField(max_length=100)
    pocket_start_date = models.DateTimeField('start date', null=True, blank=True)
    pocket_end_date = models.DateTimeField('end date', null=True, blank=True)


    def __str__(self):
        return self.balance_name
