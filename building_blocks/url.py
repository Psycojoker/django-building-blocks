from django.url import path


def to_url(view, name=None):
    return path(view.get_url_path(), view, name=name if name else view.get_url_name())
