from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__"
        fields = ["name", "comment"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "comment": forms.Textarea(attrs={'class': 'form-control', "rows": 5}),
        }
