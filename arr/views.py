from django.shortcuts import render

from arr.models import Arr

def index(request):
    arr = Arr.objects.all()
    return render(request, "arr/index.dtl", {'arr' : arr})
