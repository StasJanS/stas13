from django import forms


class InputFormStas(forms.Form):
    name0 = forms.CharField(label='name0', max_length=30)
