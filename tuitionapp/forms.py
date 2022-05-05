
from tuitionapp.models import userClass,Student,Tutor
from django import forms

class userC(forms.ModelForm):
    class Meta:
        model=userClass
        fields='__all__'

class Stud(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class Tut(forms.ModelForm):
    class Meta:
        model=Tutor
        fields='__all__'