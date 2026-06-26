from django import forms


class url_input(forms.Form):

    url = forms.CharField(label="URL")