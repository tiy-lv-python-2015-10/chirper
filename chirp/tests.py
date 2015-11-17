from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from chirp.models import Chirp


class TestChirp(TestCase):

    def setUp(self):
        user = User.objects.create_user('bob', 'bob@bob.com', password='password')
        chirp = Chirp.objects.create(author=user, message='my test message')

    def test_is_recent(self):
        chirp = Chirp.objects.first()

        self.assertTrue(chirp.is_recent())

    def test_get_tag_count(self):
        chirp = Chirp.objects.first()
        chirp.tag_set.create(name="Test1")
        chirp.tag_set.create(name="Test2")

        self.assertEqual(chirp.get_tag_count(), len(chirp.tag_set.all()))

class TestChirpList(TestCase):

    def setUp(self):
        user = User.objects.create_user('bob', 'bob@bob.com', password='password')
        chirp = Chirp.objects.create(author=user, message='my test message')

    def test_time(self):
        client = Client()
        response = client.get(reverse('list_chirps'))

        self.assertEqual(len(response.context_data['chirp_list']), 1)
        self.assertEqual(response.status_code, 200)