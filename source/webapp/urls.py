from django.urls import path

from webapp.views import CreateCV
from webapp.views.vacancies import VacancyListView, VacancyCreateView, VacancyUpdateView

urlpatterns = [
    path('vacancies', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancies/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('cv/create/', CreateCV.as_view(), name="cv_create")
]
