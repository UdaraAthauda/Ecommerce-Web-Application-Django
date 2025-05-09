from django import template

register = template.Library()

@register.filter
def item_total(value, arg):
    try:
        total = float(value) * int(arg)
        return f"{total:.2f}"
    except:
        return 'error'