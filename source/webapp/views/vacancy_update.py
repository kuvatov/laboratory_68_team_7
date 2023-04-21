from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from webapp.models import Vacancy


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    fields = ('title', 'salary', 'description', 'experience_from', 'experience_to', 'category', 'is_published')
    template_name = 'vacancy/vacancy_update.html'
    success_url = reverse_lazy('vacancy_list')
