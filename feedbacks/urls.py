from django.urls import path
from feedbacks import views

urlpatterns = [
    path('feedbacks/',views.feedbacks)
]
