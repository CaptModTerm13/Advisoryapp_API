from django import forms


class ActivityForm(forms.Form):
    activity_name = forms.CharField(label="Name of the activity", max_length=100)
    date=forms.CharField(label="Duration/Date",max_length=50)
    file=forms.FileField(label="Upload your certificate")

