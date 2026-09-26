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
<<<<<<< HEAD
    path('verify/',views.verify),
<<<<<<< Updated upstream
=======
>>>>>>> a3ec0e37fed7a60b9c57d1f1f5cc2f52bca2d287
    path('threat/',views.threat)
=======
    path('threat/',views.threat),
>>>>>>> Stashed changes
]

