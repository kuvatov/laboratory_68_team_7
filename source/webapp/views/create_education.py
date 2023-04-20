from django.shortcuts import redirect
from django.views.generic import CreateView
# from django.contrib.auth.mixins import UserPassesTestMixin

from webapp.models import Education, CV


class CreateEducation(CreateView):
    template_name = "CV/education_create.html"
    model = Education
    fields = ("graduation_date", "institution_name", "specialisation")

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        print(kwargs)
        print(args)
        pk = kwargs.get("pk")
        print(form.is_valid())
        if form.is_valid():
            self.object = form.save()
            self.object.CVs.set(CV.objects.filter(pk=pk))
            return redirect("cv_detailed", pk)
        else:
            return super().post(request, *args, **kwargs)

    # def test_func(self):
    #     if self.request.user.profile.is_corporate:
    #         return False
    #     else:
    #         return True
