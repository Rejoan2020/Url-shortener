from django import forms
from django.core.validators import URLValidator
from .validators import validate_dot_com,validate_url

class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        label="",
        validators=[validate_url],
        widget= forms.TextInput(
            attrs={
                "placeholder":"  Enter the long url",
                "class":"form-control"
            }
        )
    )

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm,self).clean()
    #     print(cleaned_data)
    
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("This URL is not valid")
    #     print(url)