from django import forms
#ClassroomFormを定義
class ClassroomForm(forms.Form):    
    availablity = forms.FileField() 
