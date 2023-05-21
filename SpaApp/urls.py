from django.urls import path, reverse_lazy
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('service/<int:pk>/', ServicesDetail.as_view(), name='service_detail'),
    path('price', PricePage.as_view(), name='price'),
    path('masters', MasterPage.as_view(), name='master_page'),
    path('contacts', ContactsPage.as_view(), name='contacts_page'),
    path('book/<int:pk>/', BookingObject.as_view(), name='book_service'),
    path('confirmation', BookingConfirmation.as_view(), name='confirmation'),
]
