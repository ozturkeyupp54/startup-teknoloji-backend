REDIRECT_URL_PATHNAME = 'home'
import uuid
import base64 
from django.contrib.auth import login
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from django.contrib.auth import get_user_model

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.urls import reverse_lazy
from user.models import User
from user.forms import UserForm
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string

from django.contrib.auth.views import LoginView, LogoutView

class FixView:
    template_name = 'user/user_form.html'
    next_page = REDIRECT_URL_PATHNAME

class UserLoginView(LoginView):
    template_name = 'user/user_login.html'
    extra_context = {'title': 'Login'} # Sayfa Başlık
    next_page = REDIRECT_URL_PATHNAME
    pass
class UserLogoutView(FixView, LogoutView):
    pass
# User Views
class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    ordering = ['-id']

class UserCreateView(CreateView):
    extra_context = {'title': 'Register'}  # Page Title
    model = User
    form_class = UserForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy(REDIRECT_URL_PATHNAME)

    # Login after registration:
    def get_success_url(self):
        user = self.object
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        verification_link = reverse('user:verify_email', kwargs={'uidb64': uid, 'token': token})
        verification_url = f"{self.request.build_absolute_uri('/')[:-1]}{verification_link}"

        # Render the email content using the template
        email_content = render_to_string('emailtemplates/verify-email.html', {
            'user': user,
            'verification_url': verification_url,
            'product': 'Startup Teknoloji',
            'token': token,
        })

        send_mail(
            'Startup Teknoloji Dünyasına Hoşgeldiniz - Email Verification',
            'E-postanızı doğrulamanız için aşağıdaki bağlantıya tıklayın:',
            'iletisim@startupteknoloji.com',
            [user.email],
            fail_silently=False,
            html_message=email_content,  # Ekledik
        )

        return super().get_success_url()


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class UserUpdateView(UpdateView):
    model = User
    permission_classes = [IsAuthenticated]
    form_class = UserForm
    template_name = 'user/user_form.html'
    context_object_name = 'form'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    
class VerifyEmailView(View):
    template_name = 'user/verify-email.html'
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()  # Fix: Use urlsafe_base64_decode from django.utils.http
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect(REDIRECT_URL_PATHNAME)
        else:
            return redirect('user:verification_failed_page')  # Redirect to a page indicating verification failure

class VerificationFailedView(TemplateView):
    template_name = 'user/verification_failed_page.html'