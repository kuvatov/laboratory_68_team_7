from django.views.generic import ListView

from webapp.models import Vacancy


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy_list.html'
    context_object_name = 'vacancies'
