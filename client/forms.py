from django import forms
from client.models import MailingClient


class ClientForm(forms.ModelForm):
    class Meta:
        model = MailingClient
        fields = '__all__'