from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import Post

UserModel = get_user_model()

def create_user():
  "Create new test user"
  return UserModel.objects.create(username='testuser', password='password')


class CreatePostRestrictedViewTestCase(TestCase):
  def setUp(self):
    self.user = create_user()

  @override_settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.AllowAllUsersModelBackend'])

  def test_restricted_view_when_not_logged_in(self):
    """
    ensures that users who are not logged in cannot access the
    create post feature of the blog
    """
    url = reverse("create_post")
    response = self.client.get(url)

    self.assertEqual(response.status_code, 403)

  def test_restricted_view_when_logged_in(self):
    """
    ensures that users who are logged in are able to 
    access the create post feature of the blog
    """
    self.client.force_login(self.user)

    url = reverse("create_post")
    response = self.client.get(url)

    self.assertNotEqual(response.status_code, 403)


class UpdatePostRestrictedViewTestCase(TestCase):
  def setUp(self):
    "Create new test user"
    self.user = create_user()
    self.post = Post.objects.create(author=self.user, title='test post', body='example body text')

  @override_settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.AllowAllUsersModelBackend'])

  def test_restricted_view_when_not_logged_in(self):
    """
    ensures that users who are not logged in cannot access the
    create post feature of the blog
    """
    url = reverse("update_post", kwargs={'pk': self.post.pk})
    response = self.client.get(url)

    self.assertEqual(response.status_code, 403)

  def test_restricted_view_when_logged_in(self):
    """
    ensures that users who are logged in are able to 
    access the create post feature of the blog
    """
    self.client.force_login(self.user)

    url = reverse("update_post", kwargs={'pk': self.post.pk})
    response = self.client.get(url)

    self.assertNotEqual(response.status_code, 403)


class DeletePostRestrictedViewTestCase(TestCase):
  def setUp(self):
    "Create new test user"
    self.user = create_user()
    self.post = Post.objects.create(author=self.user, title='test post', body='example body text')

  @override_settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.AllowAllUsersModelBackend'])

  def test_restricted_view_when_not_logged_in(self):
    """
    ensures that users who are not logged in cannot access the
    create post feature of the blog
    """
    url = reverse("delete_post", kwargs={'pk': self.post.pk})
    response = self.client.get(url)

    self.assertEqual(response.status_code, 403)

  def test_restricted_view_when_logged_in(self):
    """
    ensures that users who are logged in are able to 
    access the create post feature of the blog
    """
    self.client.force_login(self.user)

    url = reverse("delete_post", kwargs={'pk': self.post.pk})
    response = self.client.get(url)

    self.assertNotEqual(response.status_code, 403)
