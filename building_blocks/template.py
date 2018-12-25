import os
from base import View


class Template(View):
    def __init__(self, template_name, strict=False):
        if isinstance(template_name, (list, tuple)):
            self.template_names = template_name

            if template_name and not strict:
                self.template_names.append(template_name)
            else:
                self.template_name = None

        else:
            self.template_name = template_name

            if strict:  # clear all template names possibilities
                self.template_names = []

    def get_url_name(self):
        "self.name or '/path/to/some_template.html' → 'some_template'"

        if self.name:
            return self.name

        template_name = self.get_template_names()[0]
        return os.path.splitext(template_name.split("/")[-1])[0]

    def get_url(self):
        return f"{self.get_view_name()}/"


class Decorator:
    "This is the original design decorator pattern, not python's @"
    def __init__(self, target):
        self.target = target

    def __getattr__(self, attr):
        return getattr(self.target, attr)

    # I don't think I need that, don't I?
    # def __setattr__(self, attr):
        # pass


class AnotherTemplateExtension(Decorator):
    extension = None

    def __init__(self, extension=None, strict=False)
        # this allow class variable declaration/overwriting
        self.extension = extension if extension else self.extension
        self.strict = strict

    def get_template_names(self):
        template_names = self.target.get_template_names()

        other_template_names = []
        # TODO allow to replace only certain extensions
        for template_name in template_names:
            filename, _ = os.path.splitext(template_name)
            other_template_names.append(filename + self.extension)

        if not strict:
            other_template_names += template_names

        return other_template_names


class Haml(AnotherTemplateExtension):
    "Try to get all template names as .haml version first"
    extension = ".haml"


class PrependTemplateName(Decorator):
    prepend = None

    def __init__(self, prepend=None, strict=False):
        self.prepend = prepend if prepend else self.prepend
        self.strict = strict

    def get_template_names(self):
        template_names = self.target.get_template_names()

        prepend_template_names = []
        for template_name in template_names:
            prepend_template_names.append(self.prepend + filename)

        if not strict:
            prepend_template_names += template_names

        return prepend_template_names


class BootStrap(View):
    "Prepend 'boostrap/' in templates filename"
    prepend = "boostrap/"
