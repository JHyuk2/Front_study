from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        help_text="제목은 100자 이하로 작성하세요",
        widget=forms.TextInput(
            attrs={
                'class':'my-input',
                'placeholder':'제목 입력',
            }
        )
    )
    rank = forms.IntegerField(
        label ='점수',
        widget=forms.TextInput(
            attrs={
                'class':'my-input',
                'placeholder':'점수를 입력하세요',
            }
        )
    )


    class Meta:
        model = Review
        fields = '__all__'
