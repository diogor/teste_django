from django.contrib.auth.mixins import UserPassesTestMixin
from .models import ProfileChoices


class UserIsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.profile == ProfileChoices.ADMIN
