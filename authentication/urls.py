from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="emailtemplates/password_reset.html",email_template_name = "emailtemplates/password_reset_email.html",subject_template_name = "emailtemplates/password_reset_subject.txt"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="emailtemplates/email_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="emailtemplates/reset.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="emailtemplates/reset_complete.html"), name="password_reset_complete")
]
