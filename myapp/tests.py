from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your tests here.
class myModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='YOUR_USERNAME', password='YOUR_PASSWORD')
        self.token = Token.objects.create(user=self.user, key='YOUR_TOKEN_KEY') 

    fixtures = ['initial_data.json','initial_employee_data.json']

    def test_dept_api(self):
        url = reverse('datadepartment')
        auth_token = {"HTTP_AUTHORIZATION":f'Bearer {self.token.key}'} 
        response = self.client.get(url,**auth_token)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'finance')

    def test_emp_api(self):
        url = reverse('dataemployee')
        auth_token = {'HTTP_AUTHORIZATION':f'Bearer {self.token.key}'}
        response = self.client.get(url,**auth_token)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'abhishek')
