import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
    
    def test_get_file_path(self):
        file = get_file_path(None, 'test.png')
        self.assertTrue(len(file), len(self.filename))


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEqual(str(self.service), self.service.name)
    
class PositionTestCase(TestCase):

    def setUp(self):
        self.position = mommy.make('Position')

    def test_str(self):
        self.assertEqual(str(self.position), self.position.name)
    

class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee = mommy.make('Employee')

    def test_str(self):
        self.assertEqual(str(self.employee), self.employee.name)
    

class FeatureTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEqual(str(self.feature), self.feature.name)

