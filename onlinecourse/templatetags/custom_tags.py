from django import template
register = template.Library()

#For use dictionaries into template
@register.filter
def keyvalue(dict, key):    
#    return dict[key]
    try:
        return dict[key]
    except KeyError:
        return ''