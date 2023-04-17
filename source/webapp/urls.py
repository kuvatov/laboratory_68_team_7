from django.urls import path

from webapp.views.vacancies import VacancyListView, VacancyCreateView

urlpatterns = [
    path('vacancies', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create')
]
