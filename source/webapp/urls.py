from django.urls import path

from webapp.views import CreateEducation, CreateCV, DetailedCV, UpdateCV, DeleteEducation, VacancyCreateView, \
    VacancyUpdateView, VacancyUpdateDateView, VacancyDetailView, ReplyCreateView, ReplyListView, ReplyDetailView
from webapp.views import UpdateCVDate
from webapp.views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancies/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancies/<int:pk>/update_date/', VacancyUpdateDateView.as_view(), name='vacancy_update_date'),
    path('cv/create/', CreateCV.as_view(), name="cv_create"),
    path("add-education/cv/<int:pk>/", CreateEducation.as_view(), name="add_education"),
    path("cv/<int:pk>/", DetailedCV.as_view(), name="cv_detailed"),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path("cv/<int:pk>/update", UpdateCV.as_view(), name='cv_update'),
    path("delete-education/", DeleteEducation.as_view(), name="delete_education"),
    path('cv/<int:pk>/update_date/', UpdateCVDate.as_view(), name='cv_update_date'),
    path('replies/create/', ReplyCreateView.as_view(), name='reply_create'),
    path('replies/list/', ReplyListView.as_view(), name='reply_list'),
    path('replies/<int:pk>/', ReplyDetailView.as_view(), name='reply_detail'),
]
