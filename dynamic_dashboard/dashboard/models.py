from django.db import models

class Trader(models.Model):
    name = models.CharField(max_length=100)

class DataPoint(models.Model):
    trader = models.ForeignKey(Trader, related_name='data_points', on_delete=models.CASCADE)
    profit_or_loss = models.IntegerField()
    timestamp = models.DateTimeField()

