from django.views.generic import DetailView


class DetailPageView(DetailView):
    def get_template_names(self):
        return super(DetailPageView, self).get_template_names() + [
            "pages/detail.html",
            "pages/%s_detail.html" % self.object._meta.model_name,
        ]
