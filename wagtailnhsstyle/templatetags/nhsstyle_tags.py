from django import template
from django.forms.widgets import (
    Input,
    RadioSelect,
    Textarea,
    CheckboxInput,
    CheckboxSelectMultiple
)

register = template.Library()


@register.inclusion_tag('wagtailnhsstyle/breadcrumb.html', takes_context=True)
def breadcrumbs(context):
    """
    Generates an array of pages which are passed to the breadcrumb template.
    """
    page = context['page']
    site = page.get_site()
    breadcrumb_pages = []

    # Traverse the page parents with get_parent() until we hit a site root
    while page.id != site.root_page_id and not page.is_root():
        page = page.get_parent()
        breadcrumb_pages = [page] + breadcrumb_pages

    return {
        'breadcrumb_pages': breadcrumb_pages,
    }

@register.inclusion_tag('wagtailnhsstyle/forms/form.html')
def form(django_form):
    """
    Takes a django `form` and applies custom styling to it's widgets
    """

    # monkey-patch input widgets to use our custom templates
    for field in django_form:
        widget = field.field.widget
        if isinstance(widget, RadioSelect):
            widget.template_name = 'wagtailnhsstyle/forms/radio.html'
            widget.option_template_name = 'wagtailnhsstyle/forms/radio_option.html'
        elif isinstance(widget, CheckboxSelectMultiple):
            widget.template_name = 'wagtailnhsstyle/forms/checkboxes.html'
            widget.option_template_name = 'wagtailnhsstyle/forms/checkbox_option.html'
        elif isinstance(widget, CheckboxInput):
            widget.template_name = 'wagtailnhsstyle/forms/checkbox.html'
        elif isinstance(widget, Textarea):
            widget.attrs['class'] = 'nhsuk-textarea'
        elif isinstance(widget, Input):
            widget.attrs['class'] = 'nhsuk-input'

    return {
        'form': django_form,
    }
