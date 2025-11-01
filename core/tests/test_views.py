from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Fabio Coimbra',
            'email': 'fabiogc1989@gmail.com',
            'subject': 'Any Subject',
            'message': 'Any Message'
        }
        self.client = Client()
    
    def test_get_context_data(self):
        request = self.client.get(reverse_lazy('index'))
        
        self.assertTrue('services' in request.context)
        self.assertTrue('employees' in request.context)
        self.assertTrue('left_features' in request.context)
        self.assertTrue('right_features' in request.context)
    
    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data = self.data)
        self.assertEqual(request.status_code, 302)
    
    def test_form_invalid(self):
        data = {
            'name': 'Fabio Coimbra',
            'email': 'fabiogc1989@gmail.com'
        }
        request = self.client.post(reverse_lazy('index'), data = data)
        self.assertEqual(request.status_code, 302)