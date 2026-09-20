from django.urls import path
from main_template import views
urlpatterns = [
    path('main/',views.main),
    path('user_temp/',views.user_temp),
    path('admin_temp/',views.admin_temp),
    path('security_temp/',views.security_temp)
]
