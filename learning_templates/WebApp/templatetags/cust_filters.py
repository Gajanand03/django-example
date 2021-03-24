from django import template
register = template.Library()

def truncate(value):
    #Custom Filter
    result = value[0:5]
    return result
register.filter('trun5',truncate)

@register.filter(name='cut') #Decorator
def cut(value,arg):
    """
    This cuts out the values of the 'arg' from the string.
    """
    return value.replace(arg,'')
#register.filter('cut',cut)