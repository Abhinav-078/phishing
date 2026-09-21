from django.urls import path
from adm import views

urlpatterns = [
    path('mguser/',views.mguser),
    path('mganalyst/',views.mganalyst),
    path('reports/',views.reports),
    path('view_reports/',views.view_reports),
    path('reply/',views.reply),
    path('feedback/',views.feedback),
    path('security/',views.security)
]

