from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from django.views import View

from webapp.models import Education


class DeleteEducation(UserPassesTestMixin, View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        education_id = data.get("education_id")
        eduction = Education.objects.get(pk=education_id)
        eduction.delete()
        return JsonResponse(data=data, status=203)

    def test_func(self):
        data = self.request.POST
        education_id = data.get("education_id")
        eduction = Education.objects.get(pk=education_id)
        return self.request.user.CVs.all() & eduction.CVs.all()



