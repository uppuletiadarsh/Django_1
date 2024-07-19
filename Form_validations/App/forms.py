from django import forms


class Register(forms.Form):
    FirstName = forms.CharField(label='First Name')
    LastName = forms.CharField(label='Last Name')
    Email = forms.EmailField(label='Email')
    UserName = forms.CharField(label='Username')
    PassWord = forms.CharField(label='Password', widget=forms.PasswordInput())
    ConfirmPassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    Phone = forms.CharField(label='Phone', max_length=15)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('PassWord')
        a = len(password)
        confirm_password = cleaned_data.get('ConfirmPassword')
        if password != confirm_password:
            raise forms.ValidationError(" Password not matched ")
        if a<8 or a>15:
            raise forms.ValidationError("Password length should be between 8 - 15 characters")


