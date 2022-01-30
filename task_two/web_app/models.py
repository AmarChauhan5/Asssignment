from statistics import mode
from django.db import models

# Create your models here.

class Reliance(models.Model):
    date = models.DateField(null=True)
    my_open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    my_close = models.FloatField()
    wpa = models.FloatField()
    no_of_shares = models.FloatField()
    no_of_trades = models.FloatField()
    total_turn_over = models.FloatField()
    deliverable_qauntity = models.FloatField()
    p_dei_qnty_to_trade_quanty = models.FloatField()
    spread_h_l = models.FloatField()
    spread_c_o = models.FloatField()

