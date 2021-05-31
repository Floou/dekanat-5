from django import forms

from mainapp.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'name',
            'specialty',
        )
