from django import template

register = template.Library()


@register.filter(name='get_from_dict')
def get(value, arg):
    return value[arg]


@register.filter(name='parse')
def parse(value):
    return f"/booking/book/{value['id']}"
