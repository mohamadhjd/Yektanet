from django import forms


class CreateAd(forms.Form):
    advertiserID = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your unique ID"})
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "Choose your photo"})
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your title"})
    )

    url = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "enter URL"})
    )
