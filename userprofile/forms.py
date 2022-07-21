from django.contrib.auth.models import User
from django import forms


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(EditUser, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False