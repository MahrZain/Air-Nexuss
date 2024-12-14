
from django import forms
from contact.models import Contact


class contactForm(forms.Form):
    name = forms.CharField(max_length=30, label='name')
    usernamee = forms.CharField(max_length=100, label='username')
    city = forms.CharField(max_length=13, label='city')
    state = forms.CharField(widget=forms.Textarea, label='state')

    class Meta:
        model = Contact
        fields = ['name', 'username', 'city', 'state']
