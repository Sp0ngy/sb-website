from django.test import TestCase, Client
from django.urls import reverse
from ..models import *

# User need privileges in DB to create the test tables:
# GRANT ALL PRIVILEGES ON "name_of_test_db".* TO `myUser`@`localhost`;

# TODO: error in test
class TestViews(TestCase):

    # This function is run before every function test method
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home:home')

    def test_home_GET(self):

        response = self.client.get(self.home_url)

        # Checks if the HTTP Response is OK
        self.assertEqual(response.status_code, 200)

        # Checks if the correct html-template is used
        self.assertTemplateUsed(response, 'home/home.html')