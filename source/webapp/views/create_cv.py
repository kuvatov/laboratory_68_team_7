from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from webapp.models import CV


class CreateCV(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "CV/cv_create.html"
    model = CV
    fields = ("category", "title", "is_published")

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = request.user
            self.object.save()
            return redirect("account", request.user.pk)
        return redirect("cv_create")

    def test_func(self):
        return self.request.user.profile.is_corporate == False

