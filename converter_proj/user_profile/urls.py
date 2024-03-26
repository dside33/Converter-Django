# urls.py
from django.urls import path
from user_profile.views import ProfileDataView

urlpatterns = [
    path('profile/<int:pk>/', ProfileDataView.as_view(), name='profile-detail'),
]
