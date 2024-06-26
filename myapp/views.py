from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Department, Employee
from myapp.serializers import DepartmentSerializers, EmployeeSerializers
# Create your views here.

class departmentGetandPost(APIView):

    def get(self,request):
        """
            This Function is use to get all the department
        """
        dept = Department.objects.all()
        serializer = DepartmentSerializers(dept,many=True)
        return Response({'Department' : serializer.data})
    
    def post(self,request):
        """
            This Function is use to add new employees
        """
        serializer = DepartmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":f"Department : {serializer.data['name']} is Saved.."},status=status.HTTP_200_OK)
        return Response({"Message":f"Department : {serializer.data['name']} is not Saved.."},status=status.HTTP_400_BAD_REQUEST)
    
class departmentPutPatchDelete(APIView):
    
    def get(self,request,pk):   
        """
            This Function is use to get record of perticular the department
        """
        dept = Department.objects.get(pk=pk)
        serializer = DepartmentSerializers(dept)
        return Response({'Department' : serializer.data})
    
    def put(self,request,pk):
        """
            This Function is use to put record of perticular the department
        """
        dept = Department.objects.get(pk=pk)
        serializer = DepartmentSerializers(dept,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":f"Department : {serializer.data['name']} is Updated.."},status=status.HTTP_200_OK)
        return Response({"Message":f"Department : {serializer.data['name']} is not Updated.."},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        """
            This Function is use to patch record of perticular the department
        """
        dept = Department.objects.get(pk=pk)
        serializer = DepartmentSerializers(dept,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":f"{serializer.data['name']} is Updated.."},status=status.HTTP_200_OK)
        return Response({"Message":f"{serializer.data['name']} is not Updated.."},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
            This Function is use to Delete record of perticular the department
        """
        dept = Department.objects.get(pk=pk)
        if dept:
            dept.delete()
            return Response({"Message":f"Department : {dept.name} is Deleted.."},status=status.HTTP_200_OK)
        return Response({"Message":"Department is not found.."},status=status.HTTP_404_NOT_FOUND)
        
class EmployeeGetandPost(APIView):

    def get(self,request):
        """
            This Function is use to get all the employee
        """
        emp = Employee.objects.all()
        serializer = EmployeeSerializers(emp,many=True)
        return Response({"Employee":serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        """
            This Function is use to add new the employee
        """
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":f"Welcome {serializer.data['name']}!! You Are Join {serializer.data['department']} Department"},status=status.HTTP_200_OK)
        return Response({"Message" : "Enter Valid Data..."},status=status.HTTP_400_BAD_REQUEST)
    
class EmployeePutPatchDelete(APIView):
    
    def get(self,request,pk):
        """
            This Function is use to get record of perticular the employee
        """
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializers(emp)
        return Response({"Employee":  serializer.data})
    
    def put(self,request,pk):
        """
            This Function is use to put record of perticular the employee
        """
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializers(emp,data=request.data)
        if emp and serializer.is_valid():
            serializer.save()
            return Response({"Message":f"{serializer.data['name']}'s profile is Updated..."},status=status.HTTP_200_OK)
        return Response({"Message":"Employee not found or Data is invalid..."},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk):
        """
            This Function is use to patch record of perticular the employee
        """
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializers(emp,data=request.data,partial = True)
        if emp and serializer.is_valid():
            serializer.save()
            return Response({"Message":f"{serializer.data['name']}'s profile is Updated..."},status=status.HTTP_200_OK)
        return Response({"Message":"Employee not found or data is invalid..."},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
            This Function is use to delete record of perticular the employee
        """
        emp = Employee.objects.get(pk=pk)
        if emp:
            emp.delete()
            return Response({"Message":f"{emp.name} Is Resign"})
        return Response({"Message":"Employee not found"},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def Employeeofdepartment(self,pk):
    try:
        dept =  Department.objects.get(pk=pk)
        emps = Employee.objects.filter(department = dept)
        if dept and emps:
            serializer = DepartmentSerializers(dept)
            serializer2 = EmployeeSerializers(emps,many=True)
            return Response({"Department": serializer.data,"Employees": serializer2.data},status=status.HTTP_200_OK)
        elif dept and not emps:
            serializer = DepartmentSerializers(dept)
            return Response({"Department": serializer.data,"Employees":f"No Employees!! in {dept.name} department you should hire."},status=status.HTTP_200_OK)
        
    except Exception:
        return Response({"Message":"There is no Department Registerd in this id"},status=status.HTTP_404_NOT_FOUND)
