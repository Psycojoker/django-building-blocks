from django.views.generic import DetailView

from .components import DetailComponent


class DetailPageView(DetailView):
    def get_template_names(self):
        return super(DetailPageView, self).get_template_names() + [
            "pages/detail.html",
            "pages/%s_detail.html" % self.object._meta.model_name,
        ]

    def get_context_data(self, *args, **kwargs):
        context = super(DetailPageView, self).get_context_data(*args, **kwargs)
        context["component"] = DetailComponent(self.object)

        return context
