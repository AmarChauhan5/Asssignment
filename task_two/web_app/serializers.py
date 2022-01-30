from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Reliance

class RelianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reliance
        fields = ['date','my_open','high','low','my_close','wpa','no_of_shares','no_of_trades','total_turn_over','deliverable_qauntity','p_dei_qnty_to_trade_quanty','spread_h_l','spread_c_o']
