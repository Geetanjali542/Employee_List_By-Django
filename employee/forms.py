from django import forms
from .models import Employee


class AddEmployee(forms.ModelForm):
    
    name = forms.TextInput()
    designation = forms.TextInput()
    email = forms.EmailInput()
    image = forms.ImageField()
  
    
    class Meta:  #which details to be displayed and which model to be selected
        model = Employee
        fields = ["name", "designation", "email", "image"]
        
        

