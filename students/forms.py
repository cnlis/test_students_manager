from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _
from django_select2 import forms as s2forms

from students.models import Department, Student, Teacher

UNIQUE_NAME_STR = _('Фамилия, имя и отчество должны быть уникальны!')


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['last_name', 'first_name', 'middle_name', 'sex', 'department']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': UNIQUE_NAME_STR,
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        data = (
                cleaned_data.get('last_name') +
                cleaned_data.get('first_name') +
                cleaned_data.get('middle_name')
        )
        if not data.replace('-', '').isalpha():
            self.add_error(
                field='last_name',
                error=_('В фамилии, имени и отчестве должны быть буквы')
            )


class TeacherForm(StudentForm):

    class Meta:
        model = Teacher
        fields = ['last_name', 'first_name', 'middle_name', 'sex']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': UNIQUE_NAME_STR,
            }
        }


class TeachersWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'last_name__icontains',
        'first_name__icontains',
        'middle_name__icontains'
    ]


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name', 'teachers']
        widgets = {'teachers': TeachersWidget}
