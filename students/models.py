from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):

    class Sex(models.TextChoices):
        MALE = 'M', _('мужской')
        FEMALE = 'F', _('женский')

    sex = models.CharField(
        max_length=1, choices=Sex.choices, blank=False, null=False,
        default=Sex.MALE, verbose_name='Пол',
    )
    first_name = models.CharField(
        max_length=40, blank=False, null=False, verbose_name=_('Имя'),
    )
    last_name = models.CharField(
        max_length=40, blank=False, null=False, verbose_name=_('Фамилия'),
    )
    middle_name = models.CharField(
        max_length=60, blank=True, default='', verbose_name=_('Отчество'),
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):

    department = models.ForeignKey(
        'Department', on_delete=models.SET_NULL, related_name='department',
        blank=False, null=True, verbose_name=_('Кафедра'),
    )

    class Meta:
        unique_together = ['first_name', 'last_name', 'middle_name']
        verbose_name = _('студент')
        verbose_name_plural = _('студенты')
        ordering = ['last_name', 'first_name', 'middle_name']


class Teacher(Person):

    class Meta:
        unique_together = ['first_name', 'last_name', 'middle_name']
        verbose_name = _('преподаватель')
        verbose_name_plural = _('преподаватели')
        ordering = ['last_name', 'first_name', 'middle_name']


class Department(models.Model):
    name = models.CharField(
        max_length=40, blank=False, null=False, verbose_name=_('Кафедра'),
    )
    teachers = models.ManyToManyField(
        Teacher, related_name='departments', verbose_name=_('Преподаватели'), blank=True)

    class Meta:
        verbose_name = _('кафедра')
        verbose_name_plural = _('кафедры')

    def __str__(self):
        return self.name
