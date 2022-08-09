from django.urls import path,include
from . import views

urlpatterns = [
    #path('login/', views.login_view, name="login"),
    #path('profile/', views.profile, name="profile"),
    #path('register/', views.register, name='register'),
    #path('asmp/', views.asmp, name='asmp'),
    
    #path('logout', views.logout_view, name="logout"),
    path('wishlist', views.wishlist, name="wishlist"),
    path('pref', views.pref, name="pref"),
    path('', views.asmp, name="asmp"),
    #path('asmp_team', views.asmp_team, name="asmp_team"),
    path('update', views.update, name='update'),
    path('fav/<id>/', views.favourite_add, name="favourite_add"),
    path('profile', views.personal_info_add, name='ASMPprofile'),
]