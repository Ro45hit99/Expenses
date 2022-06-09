from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('index1', views.home, name = 'index1'),
    path('add', views.add, name = 'add'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('signup', views.signUp,name='signup'),
    path('', views.login,name='login'),
    path('logout', views.logout_view, name='logout'),
    path('logout', views.logout_view, name='logout')
]