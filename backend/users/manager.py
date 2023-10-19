from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **args):
        if not email:
            raise ValueError("Email is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **args)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **args):
        args.set_default("is_staff", True)
        args.set_default("is_superuser", True)
        args.set_default("is_active", True)

        self.create_user(email, password, **args)

