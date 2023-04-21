from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from webapp.models import Vacancy


class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    template_name = 'vacancy/vacancy_create.html'
    fields = ('title', 'salary', 'description', 'experience_from', 'experience_to', 'category', 'is_published')
    success_url = reverse_lazy('vacancy_list')
