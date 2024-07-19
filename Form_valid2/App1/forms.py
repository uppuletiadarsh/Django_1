from django import forms

class EmpReg(forms.Form):
    Id = forms.IntegerField()
    Name = forms.CharField()
    PassWord = forms.CharField()
    ConfirmPassword = forms.CharField()
    Dept_Id = forms.IntegerField()
    def clean(self):
        cleaned_data = super().clean()
        psw = cleaned_data.get('PassWord')
        cpsw = cleaned_data.get('ConfirmPassword')
        if psw != cpsw :
            raise forms.ValidationError('Password Not Matched')
        if len(psw) < 8 or len(psw) > 15:
            raise forms.ValidationError('Password length Should be 8-15 Characters')