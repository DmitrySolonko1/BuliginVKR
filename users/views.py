from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('main_page')
    template_name = 'users/signup.html'

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        print(self.request.user)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.username = self.request.POST.get('email')
        fields.fullname = f"{self.request.POST.get('surname')} {self.request.POST.get('name')} {self.request.POST.get('middlename')}"
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('main_page')
