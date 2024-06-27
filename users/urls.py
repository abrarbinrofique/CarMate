
from django.urls import path
from .import views

urlpatterns = [
    
    path('signup/',views.signupform,name='signup'),
    path('login/',views.loginform.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logoutform.as_view(),name='logout'),
    path('modelbuy/<int:id>',views.modelbuy,name='modelbuy')

]
