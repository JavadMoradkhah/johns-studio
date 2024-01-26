from django.core.exceptions import PermissionDenied
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='profile')
    biography = models.TextField()
    image = models.ImageField(upload_to='core/images/users')


class Service(models.Model):
    image = models.ImageField(upload_to='core/images/services')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='portfolio')
    image = models.ImageField(upload_to='core/images/portfolio')
    caption = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.caption or f'No Caption <{self.created}>'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        desired_width = 1024
        img = Image.open(self.image.path)

        if img.width > desired_width:
            shrink_percentage = desired_width * 100 // img.width
            desired_height = (img.height * shrink_percentage) / 100

            img.thumbnail((desired_width, desired_height))

            img.save(self.image.path)


class InstagramPost(models.Model):
    portfolio = models.OneToOneField(Portfolio,
                                     primary_key=True,
                                     on_delete=models.PROTECT,
                                     related_name='instagram_post'
                                     )
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)


class Slide(models.Model):
    portfolio = models.OneToOneField(Portfolio, primary_key=True, on_delete=models.PROTECT, related_name='slide')
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return 'Contact Info'

    def save(self, *args, **kwargs):
        if not self.pk and ContactInfo.objects.exists():
            raise PermissionDenied('Only one instance of contact info is allowed')

        return super(ContactInfo, self).save(*args, **kwargs)


class SocialMediaInfo(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    pinterest = models.URLField()
    behance = models.URLField()

    class Meta:
        verbose_name = 'Social Media Info'
        verbose_name_plural = 'Social Media Info'

    def __str__(self):
        return 'Social Meda Info'

    def save(self, *args, **kwargs):
        if not self.pk and SocialMediaInfo.objects.exists():
            raise PermissionDenied('Only one instance of social media info is allowed')

        return super(SocialMediaInfo, self).save(*args, **kwargs)
