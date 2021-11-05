from django.urls import path
from base.views import Home
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required

app_name = 'base'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name='logout'),
]
