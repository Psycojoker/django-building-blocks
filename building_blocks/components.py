from django.template.loader import get_template

from .fields import Field


class Component(object):
    def render(self):
        template = get_template(self.template_name)
        return template.render(self.get_context_data())


class DetailComponent(Component):
    template_name = "components/detail_component.html"

    def __init__(self, model):
        self.model = model

    def get_context_data(self):
        return {
            "component": self
        }

    def fields(self):
        for i in self.model._meta.fields:
            if i.primary_key:
                continue

            yield Field(i, model=self.model)
