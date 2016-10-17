from django import template
from django.utils.dateparse import parse_datetime
register = template.Library()


def string_to_date(value):
    