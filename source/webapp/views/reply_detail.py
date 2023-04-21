from django.views.generic.detail import DetailView

from webapp.models import Reply


class ReplyDetailView(DetailView):
    model = Reply
    template_name = 'reply/reply_detail.html'
