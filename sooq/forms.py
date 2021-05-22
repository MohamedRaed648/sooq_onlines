from django import forms
from .models import *
class Post_form(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['type_of_prodect','discripe_prod1ect','prodect_cost']

