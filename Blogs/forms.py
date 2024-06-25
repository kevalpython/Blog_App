"""
This module creates Django forms for HTML files.
"""

from django import forms

from .models import Comments, User, Blogs


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


class SignUpForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Re-enter Password"}
        )
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "biography",
            "password",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "biography": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Biography"}
                ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Password"}
            ),
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        print("print",password)
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passowrd do not match.")
        return password_confirm


class AddBlogForm(forms.ModelForm):

    class Meta:
        model = Blogs
        fields = ("title", "description")
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
        }


class Edit_BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ("title", "description")
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
        }