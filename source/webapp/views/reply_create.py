from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from webapp.forms.reply_form import ReplyForm


class ReplyCreateView(LoginRequiredMixin, CreateView):
    form_class = ReplyForm
    template_name = 'reply/reply_create.html'
    success_url = reverse_lazy('reply_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
