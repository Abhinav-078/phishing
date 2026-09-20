from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def feedbacks(request):
    return render(request,'feedbacks/feedbacks.html')