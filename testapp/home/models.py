from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import (
         ActionLinkBlock,
         CareCardBlock,
         WarningCalloutBlock,
         InsetText
)


class HomePage(Page):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('care_card', CareCardBlock()),
        ('warning_callout', WarningCalloutBlock()),
        ('inset_text', InsetText()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ChildPage(Page):
    pass
