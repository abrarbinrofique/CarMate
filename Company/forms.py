from Company.models  import companymodel
from django import forms

class companyform(forms.ModelForm):
    class Meta:
        model=companymodel
        fields='__all__'
        

  