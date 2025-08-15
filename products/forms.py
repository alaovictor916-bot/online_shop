from django import forms
from .models import Product




class Search_form(forms.Form):
    search = forms.CharField()

class sell_form(forms.ModelForm):
    class Meta :
      model = Product
      fields = [ 'title' , 'description' , 'price' , 'quantity_avail', 'image']

    

    