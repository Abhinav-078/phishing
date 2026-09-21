from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def mguser(request):
    return render(request,'adm/mguser.html')
def mganalyst(request):
    return render(request,'adm/mganalyst.html')
def reports(request):
    return render(request,'adm/reports.html')
def view_reports(request):
    return render(request,'adm/view_reports.html')
def reply(request):
    return render(request,'adm/reply.html')
def feedback(request):
    return render(request,'adm/feedback.html')
def security(request):
    return render(request,'adm/security.html')
