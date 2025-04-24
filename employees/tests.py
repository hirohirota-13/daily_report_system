from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from . import views
from .models import Employee, User

# Create your tests here.
class EmployeeModelTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username="testuser", password="password")

  def test_employee_str_with_user(self):
    employee = Employee.objects.create(
      name="Alice",
      email="alice@example.com",
      department="HR",
      user=self.user
    )
    self.assertEqual(str(employee), "Alice (testuser)")

  def test_employee_str_without_user(self):
    employee = Employee.objects.create(
      name="Bob",
      email="bob@example.com",
      department="Finance"
    )
    self.assertEqual(str(employee), "Bob (No User)")


class EmployeeViewsUnitTest(TestCase):
  def setUp(self):
    self.factory = RequestFactory()
    self.staff_user = User.objects.create_user(username="staff", password="password", is_staff=True)

  def test_employee_new_view_post_valid(self):
    data = {
      'name': 'New Employee',
      'department': 'HR',
      'email': 'newemployee@example.com',
      'username': 'newuser',
      'password': 'newpassword'
    }
    request = self.factory.post(reverse('employee_new'), data)
    request.user = self.staff_user # staff_member_required のため
    response = views.employee_new(request)
    # POST が有効ならリダイレクト(302)が返るはず
    self.assertEqual(response.status_code, 302)

