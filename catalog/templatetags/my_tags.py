from django import template

register = template.Library()


@register.filter()
def media_filter(path) -> str:
    """
    Создаем фильтр для изменения пути до изображения в шаблонах
    :param path:
    :return:path
    """
    if path:
        return f"/media/{path}"
    return "#"
