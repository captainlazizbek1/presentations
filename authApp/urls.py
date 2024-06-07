from django.urls import path
from authApp.views import RegisterView, LoginView, \
ProfileEditView, LogoutView



app_name = 'authApp'
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile_edit/', ProfileEditView.as_view(),name='profileEdit'),
    path('logout/', LogoutView.as_view(), name='logout')
]