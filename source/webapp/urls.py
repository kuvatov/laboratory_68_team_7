from django.urls import path

from webapp.views import CreateCV
from webapp.views.vacancies import VacancyCreateView, VacancyUpdateView, VacancyUpdateDateView, \
    VacancyDetailView
from webapp.views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancies/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancies/<int:pk>/update_date/', VacancyUpdateDateView.as_view(), name='vacancy_update_date'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('cv/create/', CreateCV.as_view(), name="cv_create")
]
