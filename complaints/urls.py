from django.urls import path
from complaints import views

urlpatterns = [
    path('complaints/', views.complaints)
]
