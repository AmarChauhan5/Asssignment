from django.contrib import admin
from .models import Reliance

# Register your models here.
@admin.register(Reliance)
class RelianceAdmin(admin.ModelAdmin):
    list_display = ['date','my_open','high','low','my_close','wpa','no_of_shares','no_of_trades','total_turn_over','deliverable_qauntity','p_dei_qnty_to_trade_quanty','spread_h_l','spread_c_o']
