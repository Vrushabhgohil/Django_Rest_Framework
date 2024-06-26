from django.urls import path

from myapp.views import *

urlpatterns = [
    path("department/getorpost", departmentGetandPost.as_view()),
    path("department/updateordelete/<int:pk>", departmentPutPatchDelete.as_view()),
    path("employee/getorpost", EmployeeGetandPost.as_view()),
    path("employee/updateordelete/<int:pk>", EmployeePutPatchDelete.as_view()),
    path("employee/department/<int:pk>", Employeeofdepartment),
    path("employeewithhtml/", TemplateGetEmployee.as_view(),name='employee'),
    path("departmentwithhtml/", TemplateGetDepartment.as_view(),name='department'),
    path("empofdeptwithhtml/<int:pk>", TemplateGetEmpOfDept.as_view(),name='employeeofdepartment'),
    path("employee/registration", FormEmployee.as_view(),name='employeeregistration'),
]
