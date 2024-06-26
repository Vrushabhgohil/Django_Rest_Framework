from django.urls import path

from myapp.views import EmployeeGetandPost, EmployeePutPatchDelete, Employeeofdepartment, departmentGetandPost, departmentPutPatchDelete

urlpatterns = [
    path("department/getorpost", departmentGetandPost.as_view()),
    path("department/updateordelete/<int:pk>", departmentPutPatchDelete.as_view()),
    path("employee/getorpost", EmployeeGetandPost.as_view()),
    path("employee/updateordelete/<int:pk>", EmployeePutPatchDelete.as_view()),
    path("employee/department/<int:pk>", Employeeofdepartment),
]
