from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from webapp.models import Vacancy


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy_list.html'
    context_object_name = 'vacancies'


class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    template_name = 'vacancy/vacancy_create.html'
    fields = ('title', 'salary', 'description', 'experience_from', 'experience_to', 'category', 'is_published')
    success_url = reverse_lazy('vacancy_list')


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    fields = ('title', 'salary', 'description', 'experience_from', 'experience_to', 'category', 'is_published')
    template_name = 'vacancy/vacancy_update.html'
    success_url = reverse_lazy('vacancy_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save(update_fields=['updated_at'])
        return super().form_valid(form)
