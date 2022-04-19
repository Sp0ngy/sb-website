from django.test import TestCase, Client
from django.urls import reverse
from home.models import InfoBox, Subscription

# User need privileges in DB to create the test tables:
# GRANT ALL PRIVILEGES ON "name_of_test_db".* TO `myUser`@`localhost`;

class TestViews(TestCase):

    # This function is run before every function test method
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home:home')
        self.privateservice_url = reverse('home:privateservice')
        self.partner_url = reverse('home:partner')
        self.membership_url = reverse('home:membership')
        self.infobox = InfoBox.objects.create(
            is_active=True,
            info_name='Test Info Box',
            info_text='Some test Info',
        )
        self.subscription = Subscription.objects.create(
            first_name='nico',
            last_name='schuerrle',
            email='',
            country='3',
            phone='018273773737',
            date_of_birth= '1994-09-08',
            terms_accepted= True,
        )

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        # Checks if the HTTP Response is OK
        self.assertEqual(response.status_code, 200)
        # Checks if the correct html-template is used
        self.assertTemplateUsed(response, 'home/home.html')

    def test_privateservice_GET(self):
        response = self.client.get(self.privateservice_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/private_service.html')

    def test_partner_GET(self):
        response = self.client.get(self.partner_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/partner.html')

    # Make several, separated test cases for a view with GET, POST, .. methods
    def test_membership_GET(self):
        response = self.client.get(self.membership_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/membership.html')

    def test_membership_POST_add_new_subscriber(self):
        response = self.client.post(self.membership_url, {
            'first_name': 'nico',
            'last_name': 'schuerrle',
            'email': 'asfasf@asdfa.com',
            'country': 'Germany',
            'phone': '018273773737',
            'date_of_birth': '1994-09-08',
            'terms_accepted': True,
        })

        #check if redirect works
        self.assertEqual(response.status_code, 302)
        #self.assertEqual(self.subscription.first().first_name, 'nico')

    def test_membership_POST_submit_subscriber_no_data(self):
        response = self.client.post(self.membership_url)

        self.assertEqual(response.status_code, 302)
