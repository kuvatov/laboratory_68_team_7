from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView

from webapp.models import CV


class UpdateCV(PermissionRequiredMixin, UpdateView):
    model = CV
    template_name = "CV/cv_update.html"
    context_object_name = "task"
    fields = ("category", "title", "is_published")
    context_object_name = "CV"

    def get_success_url(self):
        return reverse("cv_detailed", kwargs={"pk": self.object.pk})

    def has_permission(self):
        cv = get_object_or_404(CV, pk=self.kwargs.get("pk"))
        return self.request.user == cv.owner
