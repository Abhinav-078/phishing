from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def register(request):
    return render(request,'user/register.html')