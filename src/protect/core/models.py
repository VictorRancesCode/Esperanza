import random
import string

from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    missing = 'missing'
    found = "found"
    TYPE_PUBLICATION_CHOICES = (
        (missing, _('missing')),
        (found, _('found')),
    )
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
        ('Other', _('Other'))
    )
    email = models.EmailField(_('email address'), blank=True, help_text=_("Email of the person who is reporting"))
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    nickname = models.CharField(_('nickname'), max_length=150, blank=True)
    place = models.CharField(_('place'), max_length=150, blank=True)
    date = models.DateField(_('date'))
    photo = models.ImageField(_('photo'),upload_to='person', null=True, blank=True)
    comment_photo = models.CharField(_('comment the photo'), max_length=150, blank=True)
    age = models.IntegerField(_('age'))
    gender = models.CharField(_('gender'), max_length=150, blank=True, choices=GENDER_CHOICES, default='M')
    detail = models.CharField(_('details'), max_length=500, blank=True)
    is_active = models.BooleanField(_('active'), default=False)
    type_publication = models.CharField(_('type'), max_length=150, blank=True, choices=TYPE_PUBLICATION_CHOICES,
                                        default=missing)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.first_name

    def random_string_generator(self, size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def unique_slug_generator(self, new_slug=None):
        if new_slug is not None:
            slug = new_slug
        else:
            slug = slugify(self.first_name)
        qs_exists = Person.objects.filter(slug=slug).exists()
        if qs_exists:
            new_slug = "{slug}-{randstr}".format(
                slug=slug,
                randstr=self.random_string_generator(size=4)
            )
            return self.unique_slug_generator(new_slug=new_slug)
        return slug

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = self.unique_slug_generator()
        super(Person, self).save()


class Comment(models.Model):
    pass
