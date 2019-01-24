from django.shortcuts import render,redirect
from django.http import HttpResponse

import csv
# Create your views here.


# locals()使用技巧
 def myyear(request,year):
     return render(request,'myyear.html')



