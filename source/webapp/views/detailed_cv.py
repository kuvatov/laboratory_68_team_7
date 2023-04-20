
from django.views.generic import DetailView
from webapp.models import CV


class DetailedCV(DetailView):
    template_name = "CV/cv_detailed.html"
    model = CV
    context_object_name = "CV"
