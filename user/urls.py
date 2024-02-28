from django.urls import path
from user.views import (
    UserLoginView,
    UserLogoutView,
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    VerifyEmailView,
    VerificationFailedView
)

app_name = 'user'

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(template_name="emailtemplates/verify-email.html"), name='verify_email'),
    path('verification-failed/', VerificationFailedView.as_view(template_name="emailtemplates/verification_failed_page.html"), name='verification_failed_page'),
]
