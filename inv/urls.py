from django.urls import path
from inv.views import CategoriaView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required

app_name = 'inv'
urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaCreateView.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaUpdateView.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDeleteView.as_view(), name='categoria_delete'),
]
