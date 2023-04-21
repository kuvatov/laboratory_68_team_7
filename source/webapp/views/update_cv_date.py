from django.http import JsonResponse
from django.views import View
from webapp.models import CV

from django.utils import timezone


class UpdateCVDate(View):
    def post(self, request, *args, **kwargs):
        cv = CV.objects.get(pk=self.kwargs['pk'])
        cv.updated_at = timezone.now()
        cv.save()
        cv_id = cv.pk
        print(cv_id)
        data = {
            'updated_at': cv.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "cv_id": cv_id
        }
        return JsonResponse(data)
