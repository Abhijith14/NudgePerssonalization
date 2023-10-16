# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import authenticate

# from .models import Customer


# class AccountAuthenticationForm(forms.ModelForm):

#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     class Meta:
#         model = Customer
#         fields = ('username', 'password')

#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not authenticate(username=username, password=password):
#             raise forms.ValidationError("Invalid Login")