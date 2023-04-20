from django.views.generic import ListView

from webapp.models import Vacancy, CV


class IndexView(ListView):
    model = Vacancy
    template_name = 'index.html'
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cvs'] = CV.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)
