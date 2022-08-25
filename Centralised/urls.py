from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name='register'),
    path('asmp/', include('ASMP.urls')),
    path('coretalks/', include('Coretalks.urls')),
    path('logout', views.logout_view, name="logout"),
    path('team', views.team, name="team"),
    path('editprofile/', views.editprofile, name="editprofile")
]