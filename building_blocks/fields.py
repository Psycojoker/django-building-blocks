class Field(object):
    def __init__(self, field, model):
        self.field = field
        self.model = model
        self.name = field.verbose_name.capitalize()
        self.value = getattr(self.model, field.get_attname())

    def render(self):
        return "<b>{field.name}</b>: {field.value}".format(field=self)
