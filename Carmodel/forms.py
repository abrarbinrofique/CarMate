from Carmodel.models import car

from django import forms
from Company.models import companymodel
from Carmodel.models import comments


class carform(forms.ModelForm):
    Brandname=forms.ModelChoiceField(queryset=companymodel.objects.all(),required=True,label='Car Company')
    
    class Meta:
        model = car
        exclude = ['user','userquantity','slug']

        widgets={

              ' Brandname': forms.Select(attrs={'class': 'select'})
        }
 
class commentform(forms.ModelForm):
    class Meta:
        model=comments
        exclude = ['carmodel']

        help_texts={
            'slug':'slug must be as similar as name'
        }