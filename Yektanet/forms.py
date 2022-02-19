from django import forms

from django import forms


class CreateAd(forms.Form):
    advertiserID = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your unique ID"})
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your title"})
    )

    link = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter URL"})
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )
