from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from website.models import Hospital, Service, Specialty, Favorite


class FavoriteTest(TestCase):
    fixtures = ["test_data", 'initial_data']

    def setUp(self):
        self.user = User.objects.get(username='testuser@mail.com')

    def test_creating_favorite_with_bad_service_gives_error(self):
        user = User.objects.get(username='testuser@mail.com')
        hospital = Hospital.objects.get(name='Spitalul Clinic CFR')
        self.client.force_login(user)
        response = self.client.post(
            reverse('add_to_favorites'),
            {'hospital': hospital.name, 'specialty': 'doesntexist'})
        self.assertEqual(response.status_code, 500)

    def test_create_favorite_without_user_gives_error(self):
        hospital = Hospital.objects.get(name='Spitalul Clinic CFR')
        response = self.client.post(
            reverse('add_to_favorites'),
            {'hospital': hospital.name, 'specialty': 'doesntexist'})
        self.assertEqual(response.status_code, 500)

    def test_method_is_not_post_gives_error(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_to_favorites'))
        self.assertEqual(response.status_code, 500)

    def test_create_favorite_gives_success(self):
        user = User.objects.get(username='testuser@mail.com')
        favorites = Favorite.objects.filter(user=user)
        hospital = Hospital.objects.get(name='Spitalul Clinic CFR')
        specialty = Specialty.objects.get(name='Chirurgie Generală')
        self.client.force_login(user)
        self.client.post(
            reverse('add_to_favorites'),
            {
                'hospital': hospital.name,
                'specialty': specialty.name})
        added_favorite = Favorite.objects.filter(
            user=user,
            service__hospital=hospital,
            service__specialty=specialty).first()
        self.assertEqual(added_favorite in favorites, True)


class RemoveFromFavoriteTest(TestCase):
    fixtures = ["test_data", 'initial_data']

    def test_bad_favorite_gives_error(self):
        favorite_id = 999
        with self.assertRaises(AttributeError):
            self.client.post(
                reverse('remove_from_fav'),
                {'favorite_id': favorite_id})

    def test_favorite_is_removed_with_success(self):
        user = User.objects.get(username='testuser@mail.com')
        service = Service.objects.all().first()
        new_fav = Favorite(user=user, service=service)
        new_fav.save()
        favorite_id = new_fav.id
        response = self.client.get(
            reverse('remove_from_fav'),
            {'favorite_id': favorite_id})
        self.assertEqual(len(Favorite.objects.filter(id=favorite_id)), 0)
        self.assertEqual(response.content.decode('utf-8'), 'Favorite deleted')
