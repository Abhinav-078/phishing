from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def register(request):
    return render(request,'user/register.html')
def profile(request):
    return render(request,'user/profile.html')
def aiscore(request):
    return render(request,'user/aiscore.html')    
def detection(request):
    return render(request,'user/detection.html')
def explanation(request):
    return render(request,'user/explanation.html')
def report(request):
    return render(request,'user/report.html') 
def awareness(request):
    return render(request,'user/awareness.html')
def ask(request):
    return render(request,'user/ask.html')      
def replies(request):
    return render(request,'user/replies.html')
def history(request):
    return render(request,'user/history.html') 
def password(request):
    return render(request,'user/password.html')    