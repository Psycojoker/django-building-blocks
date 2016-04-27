from django.conf.urls import url

from .page_views import DetailPageView


class DetailPage(DetailPageView):
    @classmethod
    def as_url(klass, **kwargs):
        view = super(DetailPage, klass).as_view(**kwargs)
        model = klass.model if klass.model else kwargs.get("model")
        assert model is not None, "%s must be initialized with either a model as argument or as a class variable"
        model_name = model._meta.model_name
        return url(r"^%s/(P?<\d+>)/$" % model_name, view)
