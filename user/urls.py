from django.urls import path
from user import views

urlpatterns = [
    path('register/',views.register),
    path('profile/',views.profile),
    path('aiscore/',views.aiscore),
    path('detection/',views.detection),
    path('explanation/',views.explanation),
    path('report/',views.report),
    path('awareness/',views.awareness),
    path('ask/',views.ask),
    path('replies/',views.replies),
    path('history/',views.history),
    path('password/',views.password)
]

