from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('additional/',views.additional,name='additional'),
    path('add/',views.add,name='add'),
    path('view/',views.view,name='view'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.destroy, name='delete'),



    
]