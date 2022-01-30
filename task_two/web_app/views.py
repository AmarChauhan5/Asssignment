from django.http import HttpResponse
from django.shortcuts import render
from .models import Reliance
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from .serializers import RelianceSerializer
from .mypagination import MyPagination
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# This function are use to get the csv data from api and store into data sqllite most likly same as mysql
def put_data(request):
    url = "https://data.nasdaq.com/api/v3/datasets/BSE/BOM500325.csv?api_key=3s9tJcNpDR92v3kYK2Cy&start_date=1992-01-02"
    df = pd.read_csv(url).fillna(0.0)
    all_raw = df.to_csv().split('\n')
    print(len(all_raw[1:]))
    print(all_raw[1].split(","))
    for data in all_raw[1:]:
        # print(data.split(','))
        put_data = Reliance(
        date= data.split(",")[1],
        my_open=data.split(",")[2],
        high=data.split(",")[3],
        low=data.split(",")[4],
        my_close=data.split(",")[5],
        wpa=data.split(",")[6],
        no_of_shares=data.split(",")[7],
        no_of_trades=data.split(",")[8],
        total_turn_over=data.split(",")[9],
        deliverable_qauntity=data.split(",")[10],
        p_dei_qnty_to_trade_quanty=data.split(",")[11],
        spread_h_l=data.split(",")[12],
        spread_c_o=data.split(",")[13]
        )
        put_data.save()
    return HttpResponse("Data Saved")

# Pull Data from sqlLite database
class AllRelianceData(ListCreateAPIView):
    queryset = Reliance.objects.all()
    serializer_class = RelianceSerializer

def graph(request):
    x = Reliance.objects.values_list("date")
    y = Reliance.objects.values_list("my_close")
    fig = plt.figure()
    plt.plot(x,y)
    fig.suptitle('close v/s date time series', fontsize=14, fontweight='bold')
    plt.xlabel('YEAR', fontsize=10, fontweight='bold')
    plt.ylabel('CLOSE', fontsize=10, fontweight='bold')
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return render (request,'graph/one.html',{'data':data})

