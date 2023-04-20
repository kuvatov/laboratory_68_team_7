from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from webapp.models import Vacancy


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy_list.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


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


class VacancyUpdateDateView(View):
    def post(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(pk=self.kwargs['pk'])
        vacancy.updated_at = timezone.now()
        vacancy.save()
        return JsonResponse({'updated_at': vacancy.updated_at.strftime('%Y-%m-%d %H:%M:%S')})
