from django.test import TestCase
from .models import Business, Profile, Neighboorhood, Post, Business
from users.models import Profile
from django.contrib.auth.models import User
import datetime as dt
from django.urls import reverse

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Karen = Neighboorhood(
            hood_name='Karen', hood_location='Nairobi', hood_occupants=400)
                                               
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, Neighboorhood))

    def tearDown(self):

        Neighboorhood.objects.all().delete()

    def test_save_neighbourhood(self):

        self.new_neighbourhood.save_neighbourhood()
        self.assertTrue(len(Neighboorhood.objects.all()) > 0)

    def test_init(self):
        self.assertTrue(self.new_neighbourhood.name == 'karen')

class ProfileTestClass(TestCase):

    def setUp(self):
        self.james = Profile(
            username='joe', email='jmunyiwamwangi@gmail.com', password1='munyiwamwangi12', password2='munyiwamwangi12')

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.profile, Profile))

    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.profile.bio == "very awesome")

    def test_save_profile(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 0)