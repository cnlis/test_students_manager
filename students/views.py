from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from students.forms import StudentForm, DepartmentForm, TeacherForm
from students.models import Student, Department, Teacher

from django.utils.translation import gettext_lazy as _


class StudentList(ListView):
    model = Student
    ordering = ['last_name', 'first_name', 'middle_name']
    paginate_by = 10
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Список студентов')
        return context


class StudentDetail(UpdateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse('students:student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = _('Сохранить изменения')
        context['card_header'] = _('Информация о студенте')
        context['close_link'] = reverse('students:student_list')
        return context


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse('students:student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = _('Добавить')
        context['card_header'] = _('Добавить студента')
        context['close_link'] = reverse('students:student_list')
        return context


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:student_list')


class DepartmentList(ListView):
    model = Department
    ordering = ['name']
    paginate_by = 10
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Список кафедр')
        return context


class DepartmentDetail(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'students/student_form.html'

    def get_success_url(self):
        return reverse('students:department_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = _('Сохранить изменения')
        context['card_header'] = _('Информация о кафедре')
        context['close_link'] = reverse('students:department_list')
        return context


class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'students/student_form.html'

    def get_success_url(self):
        return reverse('students:department_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = _('Добавить')
        context['card_header'] = _('Добавить кафедру')
        context['close_link'] = reverse('students:department_list')
        return context


def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect('students:department_list')


class TeacherList(ListView):
    model = Teacher
    ordering = ['last_name', 'first_name', 'middle_name']
    paginate_by = 10
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Список преподавателей')
        return context


class TeacherDetail(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'students/student_form.html'

    def get_success_url(self):
        return reverse('students:teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = _('Сохранить изменения')
        context['card_header'] = _('Информация о преподавателе')
        context['close_link'] = reverse('students:teacher_list')
        return context


class TeacherCreate(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'students/student_form.html'

    def get_success_url(self):
        return reverse('students:teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = _('Добавить')
        context['card_header'] = _('Добавить преподавателя')
        context['close_link'] = reverse('students:teacher_list')
        return context


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('students:teacher_list')
