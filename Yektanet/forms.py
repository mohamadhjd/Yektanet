from django import forms


class CreateAd(forms.Form):
    advertiserID = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your unique ID"})
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control", "placeholder": "Choose your photo"})
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your title"})
    )

    link = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter URL"})
    )
