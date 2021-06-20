from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(cor , cart):
    keys = cart.keys()
    for id in keys :
        if int(id) == cor.id:
            return True
    return False;
