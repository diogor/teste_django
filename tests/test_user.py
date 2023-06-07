from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.test import TestCase
from apps.users.models import User


class UserCreationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test"
        )

    def test_create_user_has_default_group(self):
        self.assertEqual(self.user.groups.count(), 1)
        self.assertEqual(self.user.groups.first().name, "Reader")

    def test_reader_user_cannot_create_project(self):
        self.assertFalse(self.user.has_perm("projects.add_project"))
        self.assertFalse(self.user.has_perm("projects.change_project"))
        self.assertFalse(self.user.has_perm("projects.delete_project"))

    def test_change_user_group_give_perms(self):
        group = Group.objects.get(name="Editor")
        self.user.groups.add(group)

        self.assertTrue(self.user.has_perm("projects.add_project"))
        self.assertTrue(self.user.has_perm("projects.change_project"))
        self.assertTrue(self.user.has_perm("projects.delete_project"))

    def test_change_user_group_remove_perms(self):
        group = Group.objects.get(name="Editor")

        self.assertFalse(self.user.has_perm("projects.add_project"))
        self.assertFalse(self.user.has_perm("projects.change_project"))

        self.user.groups.add(group)

        # necessário para atualizar as permissões evitando o uso de cache
        user = get_object_or_404(User, pk=self.user.pk)

        self.assertTrue(user.has_perm("projects.add_project"))
        self.assertTrue(user.has_perm("projects.change_project"))

        self.user.groups.remove(group)

        user = get_object_or_404(User, pk=self.user.pk)

        self.assertFalse(self.user.has_perm("projects.add_project"))
        self.assertFalse(self.user.has_perm("projects.change_project"))
