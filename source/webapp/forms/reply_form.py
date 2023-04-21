from django import forms

from webapp.models import Reply


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('cv',)
