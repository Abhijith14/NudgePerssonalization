from urllib.parse import urlencode
from django import template

register = template.Library()

@register.filter
def encode_get_parameters(value):
    return urlencode(value)
