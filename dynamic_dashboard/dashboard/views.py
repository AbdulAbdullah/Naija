from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from datetime import datetime
import random
from .models import Trader

class UpdateData(View):
    def get(self, request):
        traders = Trader.objects.all()
        for trader in traders:
            profit_or_loss = random.randint(-50, 50)  # Simulate profit or loss
            timestamp = datetime.now()
            trader.data_points.create(profit_or_loss=profit_or_loss, timestamp=timestamp)
        return JsonResponse({'status': 'success'})

class UserDashboard(View):
    def get(self, request, trader_id):
        trader = Trader.objects.get(id=trader_id)
        data_points = trader.data_points.all()
        data = [{'timestamp': point.timestamp, 'profit_or_loss': point.profit_or_loss} for point in data_points]
        return JsonResponse({'data': data})
