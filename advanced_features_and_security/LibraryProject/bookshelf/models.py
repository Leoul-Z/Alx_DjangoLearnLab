from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# -------------------------------
# Custom User Manager
# -------------------------------


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


# -------------------------------
# Custom User Model
# -------------------------------
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# -------------------------------
# Example Book Model
# -------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    # Link book to a user (foreign key to custom user)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} by {self.author}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
