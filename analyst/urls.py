from django.urls import path
from analyst import views

urlpatterns = [
    path('profile/',views.profile),
    path('security/',views.security),
    path('dethistory/',views.dethistory),
    path('doubt/',views.doubt),
    path('trends/',views.trends),
    path('aiscore/',views.aiscore),
    path('records/',views.records),
    path('analys/',views.analys),
    path('report/',views.report),
    path('threat/',views.threat)
]

