from django.contrib.auth.models import Group
from django.test import TestCase
from apps.users.models import User


class UserCreationTests(TestCase):
    def test_create_user_has_default_group(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@email.com",
            password="testpassword",
            address="testaddress",
            city="testcity",
            state="teststate",
        )
        self.assertEqual(user.groups.count(), 1)
        self.assertEqual(user.groups.first().name, "Reader")

    def test_reader_user_cannot_create_project(self):
        user = User.objects.create_user(
            username="testuser", email="e@e.com", password="testpassword"
        )
        self.assertFalse(user.has_perm("projects.add_project"))
        self.assertFalse(user.has_perm("projects.change_project"))
        self.assertFalse(user.has_perm("projects.delete_project"))

    def test_change_user_group_give_perms(self):
        user = User.objects.create_user(
            username="testuser", email="e@e.com", password="testpassword"
        )

        group = Group.objects.get(name="Editor")
        user.groups.add(group)

        self.assertTrue(user.has_perm("projects.add_project"))
        self.assertTrue(user.has_perm("projects.change_project"))
        self.assertTrue(user.has_perm("projects.delete_project"))

    def test_change_user_group_remove_perms(self):
        user = User.objects.create_user(
            username="testuser", email="d@d.com", password="testpassword"
        )

        editor_group = Group.objects.get(name="Editor")

        self.assertFalse(user.has_perm("projects.add_project"))
        self.assertFalse(user.has_perm("projects.change_project"))

        user.groups.add(editor_group)

        self.assertTrue(user.has_perm("projects.add_project"))
        self.assertTrue(user.has_perm("projects.change_project"))

        user.groups.remove(editor_group)

        self.assertFalse(user.has_perm("projects.add_project"))
        self.assertFalse(user.has_perm("projects.change_project"))
