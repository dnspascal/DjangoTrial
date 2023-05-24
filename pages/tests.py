from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        responses = self.client.get('/')
        responses.assertEqual(responses.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        response.assertEqual(response.status_code, 200)
