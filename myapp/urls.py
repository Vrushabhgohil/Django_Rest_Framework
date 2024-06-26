from django.urls import path
from myapp.views import *


urlpatterns = [
    path('department/getorpost',departmentGetandPost.as_view(),name='datadepartment'),
    path("departmentwithhtml/", TemplateGetDepartment.as_view(),name='department'),
    path("department/updateordelete/<int:pk>", departmentPutPatchDelete.as_view()),
    path("department/registration", FormDepartment.as_view(),name='departmentregistration'),
    path("empofdeptwithhtml/<int:pk>", TemplateGetEmpOfDept.as_view(),name='employeeofdepartment'),
    path("employee/getorpost", EmployeeGetandPost.as_view(),name='dataemployee'),
    path("employee/updateordelete/<int:pk>", EmployeePutPatchDelete.as_view()),
    path("employee/department/<int:pk>", Employeeofdepartment),
    path("employeewithhtml/", TemplateGetEmployee.as_view(),name='employee'),
    path("employee/registration", FormEmployee.as_view(),name='employeeregistration'),
]   
