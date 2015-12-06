from django.test import TestCase

# Create your tests here.
class PredictionTest(TestCase):
	def test_home(self):
		r=self.client.get('/')
		self.assertEqual(r.status_code, 200)

def test_less_logic_page(self):
	r=self.client.get('/user/')
	self.assertEqual(r.status_code, 200)


