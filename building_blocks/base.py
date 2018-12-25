from django.template.loader import select_template

from .fields import Field

# notes:
# * handling different http verbs like GET/POST/PUT/DELETE

# > The view worklofw:
# pre-call
# def some_view(request, *args, **kwargs):
#     # pre body
#     # body (like queries and all)
#     # post body
#     # render template
#     # post render ?
#     # return

class View:
    template_name = None
    template_names = []

    self.components = []

    # view workflow
    def __call__(self, request, *args, **kwargs):
        context = {}

        # things like user permissions typically put into a decorator
        context = self.pre_call(request, context, *args, **kwargs)

        # things at the beginning of the view coe
        context = self.pre_body(request, context, *args, **kwargs)

        # where you generally do the queries and populate the context
        context = self.body(request, context, *args, **kwargs)

        # once you get the data from the database
        context = self.post_body(request, context, *args, **kwargs)

        template = self.render_template(request, context, *args, **kwargs)

        # if you ever need to modify the template
        template = self.post_render_template(request, context, template, *args, **kwargs)

        return template

    def pre_call(request, context, *args, **kwargs):
        for function in pre_call_functions:
            context = function(request, context, args, kwargs)

        return context

    def pre_body(request, context, *args, **kwargs):
        for function in pre_body_functions:
            context = function(request, context, args, kwargs)

        return context

    def body(request, context, *args, **kwargs):
        for function in body_functions:
            context = function(request, context, args, kwargs)

        return context

    def post_body(request, context, *args, **kwargs):
        for function in post_body_functions:
            context = function(request, context, args, kwargs)

        return context

    def render_template(self, request, context, *args, **kwargs):
        template = select_template(self.get_template_names())
        return template.render(self.get_context_data(), request=request)

    def post_render_template(request, context, template, *args, **kwargs):
        for function in post_render_template_functions:
            context = function(request, context, args, kwargs)

        return context

    # view functions aggregation
    pre_call_functions = []
    pre_body_functions = []
    body_functions = []
    post_body_functions = []
    post_render_template_functions = []

    def pre_call(self):
        def wrap(function):
            self.pre_call_functions.append(function)
            return function
        return wrap

    def pre_body(self):
        def wrap(function):
            self.pre_body_functions.append(function)
            return function
        return wrap

    def body(self):
        def wrap(function):
            self.body_functions.append(function)
            return function
        return wrap

    def post_body(self):
        def wrap(function):
            self.post_body_functions.append(function)
            return function
        return wrap

    def post_render_template(self):
        def wrap(function):
            self.post_render_template_functions.append(function)
            return function
        return wrap

    def get_template_names(self):
        template_names = []
        if template_name:
            template_names.append(self.template_name)

        if self.template_names:
            template_names += self.template_names

        return template_names

    def __add__(self, other):
        if not self.components:
            self.components = [self]
        self.components.append(other)

        self.pre_call_functions += other.pre_call_functions
        self.pre_body_functions += other.pre_body_functions
        self.body_functions += other.body_functions
        self.post_body_functions += other.post_body_functions
        self.post_render_template_functions += other.post_render_template_functions


# objectif: Model(Organization) + Model(User)
class Model(View):
    def __init__(self, model):
        self.model = model

    @View.body
    def get_object(self, request, context, *args, **kwargs):
        key = None
        # TODO allow custom name
        for potential_key in (f"{model._meta.name}_pk", "pk", "id"):
            if potential_key in kwargs:
                object_id = kwargs[potential_key]
                del kwargs[object_id]  # remove it so we avoid colision with other Model/Query/Other
                break

        object_ = get_object_or_404(Model, object_id)

        # only declare yourself as "object" if I'm the first
        if "object" not in context:
            context["object"] = object_

        # XXX what to do when shadowing something in the context?
        # TODO allow custom/additional names
        context[f"{model._meta.name}"] = object_

        return context