from django.urls import path

from .views import *

urlpatterns = [
    path('equipment/', EquipmentList.as_view(), name='equipment'),
    path('equipment_api/', EquipmentView.as_view()),
    path('equipment_api/<int:pk>', EquipmentView.as_view()),
    path('staff/', StaffList.as_view(), name='staff'),
    path('', MainPage.as_view(), name='main_page'),
    path('register/', RegisterFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('logout/', LogoutView.as_view()),
]