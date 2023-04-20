from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from webapp.models import Reply


class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ['resume', 'message']
    template_name = 'application_form.html'
    success_url = reverse_lazy('application_list')

    def form_valid(self, form):
        form.instance.vacancy_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReplyListView(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'application_list.html'

    def get_queryset(self):
        return Reply.objects.filter(user=self.request.user)


class ReplyDetailView(LoginRequiredMixin, DetailView):
    model = Reply
    template_name = 'application_detail.html'

    def get_queryset(self):
        return Reply.objects.filter(user=self.request.user)
