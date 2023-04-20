from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from webapp.models import Education, CV


class CreateEducation(UserPassesTestMixin, CreateView):
    template_name = "CV/education_create.html"
    model = Education
    fields = ("graduation_date", "institution_name", "specialisation")

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        pk = kwargs.get("pk")
        if form.is_valid():
            self.object = form.save()
            self.CV_object = CV.objects.filter(pk=pk)
            self.object.CVs.set(self.CV_object)
            return redirect("cv_detailed", pk)
        else:
            return super().post(request, *args, **kwargs)

    def test_func(self):
        if self.request.user.CVs.filter(pk=self.kwargs.get("pk")):
            return True
        else:
            return False
