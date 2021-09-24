from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(value, arg):
    return value.as_widget(attrs={"class": arg})


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value

    return dict_.urlencode()
