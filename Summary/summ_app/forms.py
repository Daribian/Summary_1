from django import forms

class UserForm(forms.Form):
     Имя = forms.CharField(widget=forms.TextInput(attrs={'class' : 'my_name_class'}),max_length=100, required=True)
     Фамилия = forms.CharField(widget=forms.TextInput(attrs={'class' : 'my_last_lass'}), max_length=100, required=True)
     email= forms.EmailField(widget=forms.TextInput(attrs={'class' : 'my_email_class'}), required=True)
