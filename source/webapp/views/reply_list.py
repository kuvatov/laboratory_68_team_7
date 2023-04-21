from django.views.generic.list import ListView

from webapp.models import Reply


class ReplyListView(ListView):
    model = Reply
    template_name = 'reply/reply_list.html'

    def get_queryset(self):
        return Reply.objects.filter(user=self.request.user)
