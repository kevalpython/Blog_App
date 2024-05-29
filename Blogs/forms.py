from django import forms
from .models import *

class Add_Comment_Form(forms.ModelForm):

    class Meta:
        model = Comments
        fields = (
            "comment",

        )
        widgets = {
            "comment": forms.TextInput(
                attrs={"placeholder": "give comments"}
            ),            
        }
