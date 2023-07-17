from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'address')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username']=forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
        self.fields['email']=forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
        self.fields['first_name']=forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))   
        self.fields['last_name']=forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
        self.fields['phone_number']=forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class':'form-control'}))
        self.fields['address']=forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control'}))
        self.fields['password1']=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
        self.fields['password2']=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Phone number already exists')
        return phone_number
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError('First name must be alphabetic')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError('Last name must be alphabetic')
        return last_name
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password does not match')
        return password2
    
    
    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'], 
            self.cleaned_data['phone_number'],
            self.cleaned_data['address'],
            self.cleaned_data['password2']
        )
        return user
      
class CustomEmailAuthenticationForm( forms.Form):
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
        self.password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not exist')
        return email
    
    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            if not user.check_password(password):
                raise forms.ValidationError('Password does not match')
        return password
    
    