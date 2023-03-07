from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator
import re
from webapp.models.articles import Task


def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError("Максимальная длина строки 20 символов")
    return string


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=20):
        message = 'максимальное значение %(limit_value) Вы ввели %(show_value)'
        super(CustomLengthValidator, self).__init__(limit_value, message=message)

    def compare(self, value, limit_vale):
        print(value)

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    summary = forms.CharField(
        max_length=123,
        validators=(MinLengthValidator(limit_value=2, message='Малая длина'),
                    CustomLengthValidator(limit_value=10),
                    max_length_validator)
                    )

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')

        if re.match(r'\d', summary):
            raise ValidationError('Не должно начинаться с цифры')

        if Task.objects.filter(summary=summary).exists():
            raise ValidationError('Запись с таким заголовком уже существует')

        return summary