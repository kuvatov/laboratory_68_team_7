from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from webapp.models import Reply


class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ['cv']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.vacancy_id = self.request.POST.get('vacancy_id')
        form.instance.cv_id = self.request.POST.get('cv_id')
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
