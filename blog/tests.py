from rest_framework import status
from django.urls import reverse
from django.test import TestCase

# Create your tests here.

class TestBlog_View(TestCase):
    def setUp(self) :

        self.client.login(username="adminjhsagsss",password="asdfgj")

    def test_authentication_required(self):
        self.client.logout()
        url=reverse("aricle_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)