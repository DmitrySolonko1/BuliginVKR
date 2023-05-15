from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registration', SignUpView.as_view(), name='registrations'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('main_page')), name='logout'),
    path('login', LoginUser.as_view(), name='login')
]
