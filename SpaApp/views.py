from django.shortcuts import render, redirect
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models.functions import Lower
from .forms import DateTimeForm

class MainPage(ListView):
    template_name = 'SpaApp/MainPage.html'
    model = Services
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_contains_query'] = self.request.GET.get('title_contains')
        if context['title_contains_query'] != None and context['title_contains_query'] != '':
            context['products_data'] = Services.objects.filter(title__icontains=context['title_contains_query'].lower())
        else:
            context['products_data'] = Services.objects.all().order_by('-pk')
        return context

    def get_queryset(self):
        return Services.objects.all().order_by('-pk')


class ServicesDetail(DetailView):
    model = Services
    template_name = 'SpaApp/ProductPage.html'
    context_object_name = 'service'


class PricePage(ListView):
    template_name = 'SpaApp/PricePage.html'
    model = Services
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_contains_query'] = self.request.GET.get('title_contains')
        if context['title_contains_query'] != None and context['title_contains_query'] != '':
            context['products_data'] = Services.objects.filter(title__icontains=context['title_contains_query'].lower())
        else:
            context['products_data'] = Services.objects.all().order_by('-pk')
        return context


class MasterPage(ListView):
    template_name = 'SpaApp/MastersPage.html'
    model = Masters
    context_object_name = 'masters'

    def get_queryset(self):
        return Masters.objects.all().order_by('-pk')

class ContactsPage(TemplateView):
    template_name = 'SpaApp/Contacts.html'


class BookingObject(DetailView):
    model = Services
    template_name = 'SpaApp/BookingService.html'
    context_object_name = 'service'
    form_class = DateTimeForm  # Добавляем кастомную форму

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        masters = service.specialists.all()
        print(masters)
        context['form'] = DateTimeForm(masters=masters)  # Добавляем форму в контекст
        return context

    def post(self, request, pk):
        if request.method == 'POST':
            form = DateTimeForm(request.POST)
            if form.is_valid():
                time_slot = TimeSlot.objects.create(time=form.cleaned_data['time'])
                master = form.cleaned_data['master']
                print(master)
                booking = Booking.objects.create(service=self.get_object(), time_slot=time_slot,
                                                 client_name=request.user, masters=master)
                return redirect('confirmation')
            else:
                form = DateTimeForm()
                return redirect('main_page')


class BookingConfirmation(TemplateView):
    template_name = 'SpaApp/BookingConfirmation.html'
