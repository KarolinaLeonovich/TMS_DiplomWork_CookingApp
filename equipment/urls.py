from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('equipment_api', EquipmentViewSet, basename='equipment_api')


urlpatterns = [
    path('equipment/', EquipmentList.as_view(), name='equipment'),
    path('staff/', StaffList.as_view(), name='staff'),
    path('', MainPage.as_view(), name='main_page'),
    path('register/', RegisterFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('logout/', LogoutView.as_view(next_page='/')),
    path('equipment_api/', include(router.urls)),
]