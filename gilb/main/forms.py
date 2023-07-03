from captcha.fields import CaptchaField
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label="Контакт для обратной связи ", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Содержание письма: ", widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
    captcha = CaptchaField()
