from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class myModelTestCase(TestCase):
    fixtures = ['initial_data.json','initial_employee_data.json']
    def test_dept_api(self):
        url = reverse('datadepartment')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'finance')
    
    def test_emp_api(self):
        url = reverse('employee')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'abhisek')