from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('test/',TestStatus.as_view(),name='test_status'),
    path('logout/',Logout.as_view(),name='logout'),
    path('signup/',SignUp.as_view(),name='signup'),
    path('emplist/',EmployeeList.as_view(),name='emplist'),
    path('empcreate/',EmployeeCreate.as_view(),name='empcreate'),
    path('empupdate/<int:pk>/',EmplyeeUpdate.as_view(),name='empupdate'),
    path('empdelete/<int:pk>',EmployeeDelete.as_view(),name='empdelete'),
    path('empretrive/<int:pk>/',EmployeeRertive.as_view(),name='empretrive'),

]