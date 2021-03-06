"""hack21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

# from user import views 
from accounts import views
from profiles import views as profileviews
urlpatterns = [
    # path('', TemplateView.as_view(template_name="login.html")),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account'),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('social_django.urls', namespace='social')),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordreset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='passwordreset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='passwordreset/password_reset_form.html'), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
     name='password_reset_complete'),


    path('profile/', profileviews.participant_profile_creation_view, name='profile'),
    
    path('profile_done/', profileviews.participant_profile_updated_view, name='profile_created'),

]
