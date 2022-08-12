from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm): #유효성 검사
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        def cleanpassword2(self):
            # clean필드명 형태의 메서드이다. 각 필드의 clean메서드가 호출된 후에 호출된다. 유효성 검사나 조작을 하고 싶을 때 사용한다.
            # 여기에서는 비밀번호 재확인을 위해 사용했다.
            # cleaned_data에서 필드값을 꺼내서 사용해야 한다.
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords not matched!')
            return cd['password2']