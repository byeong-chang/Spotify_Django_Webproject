from django import template

# 사용자 정의함수
register = template.Library()

@register.filter
def class_name(value):
    return value.__class__.__name__