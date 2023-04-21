from django.http import JsonResponse
from django.utils import timezone
from django.views import View

from webapp.models import Vacancy


class VacancyUpdateDateView(View):
    def post(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(pk=self.kwargs['pk'])
        vacancy.updated_at = timezone.now()
        vacancy.save()
        vacancy_id = vacancy.pk
        data = {
            'updated_at': vacancy.updated_at.strftime('%d %B %Y г. %H:%M'),
            "vacancy_id": vacancy_id
        }
        return JsonResponse(data)
