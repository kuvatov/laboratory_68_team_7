from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from webapp.models import Vacancy


class VacancyDetailView(LoginRequiredMixin, DetailView):
    model = Vacancy
    template_name = 'vacancy/vacancy_detail.html'
    context_object_name = 'vacancy'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True).order_by('-updated_at')
