from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def fun1(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'key1':obj,'key2':obj2})
