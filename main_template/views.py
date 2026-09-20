from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def main(request):
    return render(request,'main_templates/main.html')
def user_temp(request):
    return render(request,'main_templates/user.html')
def admin_temp(request):
    return render(request,'main_templates/admin.html')
def security_temp(request):
    return render(request,'main_templates/securityanalyst.html')