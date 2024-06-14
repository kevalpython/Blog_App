"""
This module creates Django forms for HTML files.
"""

from django import forms

from .models import Comments


class AddCommentForm(forms.ModelForm):
    """
    A form class for adding comments to blog posts.

    This form provides a field for users to input comments on blog posts.
    """

    class Meta:
        """
        Metadata options for the AddCommentForm.
        """

        model = Comments
        fields = ("comment",)
        widgets = {
            "comment": forms.TextInput(attrs={"placeholder": "give comments"}),
        }
