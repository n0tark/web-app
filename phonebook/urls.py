from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactListView)
router.register(r'appinfo', views.AppInfoView)
router.register(r'profile', views.ProfileView)
router.register(r'register', views.RegisterView)
router.register(r'login', views.RegisterView)

urlpatterns = [
    path('', views.phonebook, name='phonebook'),
    path('delete/<int:pk>/', views.delete_contact, name='delete'),
]

urlpatterns += router.urls