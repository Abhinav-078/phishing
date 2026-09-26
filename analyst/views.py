from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return render(request,'analyst/profile.html')
def security(request):
    return render(request,'analyst/security.html')
def dethistory(request):
    return render(request,'analyst/dethistory.html')
def doubt(request):
    return render(request,'analyst/doubt.html')
def trends(request):
    return render(request,'analyst/trends.html')
def aiscore(request):
    return render(request,'analyst/aiscore.html')
def records(request):
    return render(request,'analyst/records.html')
def analys(request):
    return render(request,'analyst/analys.html')
def report(request):
    return render(request,'analyst/report.html')
def verify(request):
    return render(request,'analyst/verify.html')
def threat(request):
    return render(request,'analyst/threat.html')
