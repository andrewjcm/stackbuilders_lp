from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    contact_email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('contact_email'),
        FieldPanel('address'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('phone'),
    ]