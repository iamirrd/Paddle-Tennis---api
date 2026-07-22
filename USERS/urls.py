from django.urls import path
from .api_views import (
    RegisterView,
    LogoutView,
    ProfileView,
    ChangePasswordView,
)

urlpatterns = [
    path('register/'        , RegisterView.as_view()        , name='register'),
    path('logout/'          , LogoutView.as_view()          , name='logout'),
    path('profile/'         , ProfileView.as_view()         , name='profile'),
    path('change-password/' , ChangePasswordView.as_view()  , name='change-password'),
]