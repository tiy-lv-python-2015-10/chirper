from django.contrib.auth.models import User
from django.test import TestCase
from chirp.models import Chirp


class TestChirp(TestCase):

    def setUp(self):
        user = User.objects.create_user('bob', 'bob@bob.com', password='password')
        chirp = Chirp.objects.create(author=user, message='my test message')

    def test_is_recent(self):
        chirp = Chirp.objects.get(pk=1)

        self.assertTrue(chirp.is_recent())

    def test_get_tag_count(self):
        chirp = Chirp.objects.get(pk=1)
        chirp.tag_set.create(name="Test1")
        chirp.tag_set.create(name="Test2")

        self.assertEqual(chirp.get_tag_count(), len(chirp.tag_set.all()))