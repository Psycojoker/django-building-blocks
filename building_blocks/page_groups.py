from django.conf.urls import url

from .pages import DetailPage


class CRUD(DetailPage):
    DetailPage = DetailPage

    @classmethod
    def as_urls(klass, **kwargs):
        return [x.as_url(**kwargs) for x in (klass.DetailPage,)]
