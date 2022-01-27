from django import template

register = template.Library()

# see https://docs.djangoproject.com/en/dev/howto/custom-template-tags/
@register.simple_tag
def get_verbose_field_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()