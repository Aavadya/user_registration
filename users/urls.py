
from django.urls import path
from .views import patient_signup, doctor_signup,patient_dashboard,doctor_dashboard,doctor_login,patient_login,user_login


urlpatterns = [
    path('',user_login , name='user_login'),
    path('patient_signup/', patient_signup, name='patient_signup'),
    path('doctor_signup/', doctor_signup, name='doctor_signup'),
    path('patient_login/', patient_login, name='patient_login'),
    path('doctor_login/', doctor_login, name='doctor_login'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
]
