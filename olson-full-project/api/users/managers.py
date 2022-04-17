from django.contrib.auth.base_user import BaseUserManager

# Custom manager.
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            is_active=True, 
            is_superuser=True,
            is_staff=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user