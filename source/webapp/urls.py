from django.urls import path

from webapp.views import CreateEducation, CreateCV, DetailedCV
from webapp.views.vacancies import VacancyListView, VacancyCreateView, VacancyUpdateView, VacancyUpdateDateView

urlpatterns = [
    path('vacancies', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancies/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancies/<int:pk>/update_date/', VacancyUpdateDateView.as_view(), name='vacancy_update_date'),
    path('cv/create/', CreateCV.as_view(), name="cv_create"),
    path("add-education/cv/<int:pk>/", CreateEducation.as_view(), name="add_education"),
    path("cv/<int:pk>/", DetailedCV.as_view(), name="cv_detailed")
]
