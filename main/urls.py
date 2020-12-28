from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name='home'),
	path('about-uni', views.about, name='about'),
	path('city', views.city, name='city'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
