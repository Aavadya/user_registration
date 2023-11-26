
from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls'))
    
    
]
