"""
URL configuration for phish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('analyst/',include('analyst.urls')),
    path('application/',include('application.urls')),
    path('complaints/',include('complaints.urls')),
    path('doubt/',include('doubt.urls')),
    path('email_phno/',include('email_phno.urls')),
    path('feedbacks/',include('feedbacks.urls')),
    path('login/',include('login.urls')),
    path('phishing/',include('phishing.urls')),
    path('user/',include('user.urls')),
    path('website/',include('website.urls')),
    path('main_template/',include('main_template.urls'))
]
