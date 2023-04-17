from django.urls import path

from webapp.views.vacancies import VacancyListView

urlpatterns = [
    path('vacancies', VacancyListView.as_view(), name='vacancy_list')
]
