from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('create/', views.StudentCreate.as_view(), name='student_create'),
    path('<int:pk>/delete/', views.delete_student, name='student_delete'),

    path('departments/', views.DepartmentList.as_view(), name='department_list'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department_detail'),
    path('departments/create/', views.DepartmentCreate.as_view(), name='department_create'),
    path('departments/<int:pk>/delete/', views.delete_department, name='department_delete'),

    path('teachers/', views.TeacherList.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view(), name='teacher_detail'),
    path('teachers/create/', views.TeacherCreate.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/delete/', views.delete_teacher, name='teacher_delete'),
]
