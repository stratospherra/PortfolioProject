from django.urls import path
from .views import SignUpView, ProfileDetailView, ProfileUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('update_profile/<int:pk>', ProfileUpdateView.as_view(), name='update_profile')
]
