from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)

    class Meta:
        model = Student
        #fields = "__all__"   包含model中所有属性
        #控制在表单中只显示6个属性
        fields = (
            'name','sex','profession',
            'email','qq','phone'
        )
