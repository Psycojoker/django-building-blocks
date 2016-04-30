**NEARLY NOTHING BELLOW IS IMPLEMENTED YET**. Those are more notes for me.

# Objective

Add the missing layer of abstractions that django doesn't provide
for reusability with customizability in mind.

# Approach

Continue to work started by generic views and adding the missing abstractions
of top of it until they are enough to rebuild the django-admin.  Those
abstractions go both vertical (on top of) and horizontally (allowing fine grain
customization).

# New layers of abstractions

## Vertical abstractions

The vertical new layers of abstractions (the more obvious one) are the
continuation of generic views. If we see generic view has "data" + "view", the
next layers each add one needed concept to it:

* generic views: data (model or template name) + view
* page view: generic view + default template
* page: page view + default url
* page group: a collection of pages (for example: CRUD on a model like in django-admin)

## Horizontal abstractions

Horizontal abstractions are less obvious be needed to offer way greater
flexibility. They can be called "fine grained abstractions".

* component: like a page view but renders itself inside an already existing template (while a page view have a whole page template)
* field: renders a field of a model
* input: same but for input

## Blabla

Actually, a page view is just a template that renders a component. The
flexibility comes from the fact that you can have page (view) with several
components inside of it (for example you could easily include a
ResearchBarComponent along a LoginFormComponent and a MenuComponent in you page
displaying a ListComponent).

# Static files dependancies

Every component, fields and input can specify javascript/css files they needs
to operate (the templates that include them is responsible for specifying where
the html code declaring those dependancies is rendered).

# Global settings

The last concept introduce by django-building-blocks is global settings that
are here to allow to specify the global behavior of the building blocks.

This include mostly:

* choosing the them used for the templates (for example: default, django-admin, bootstrap, foundation or other)
* the only other thing I could think about right now is a global menu for your whole website

# Ideas of good to have abstractions

* CRUD: list\*, create\*, delete\*, update\*, detail\*, table\* (for table displaying like in django-admin)
* Regroup\* (behaving like the templatetag regroup)
* search\*
* MenuComponent
* HistoryComponent
* AuthenticationPageGroup
* RegistrationPageGroup (for django-registration)
* ContactPage
* maybe common patterns could be supplied like Comment\* and Post\*

# History

This idea originate from a talk from Ola about how unflexible the django-admin
was and that this would be great if it changed a bit combine with my need to be
able to write a lot of simple but customizable backoffice tools and being
frustrated by django-admin (despite its awesomeness).

Original draft: https://gist.github.com/Psycojoker/03de40a4ca0833919be7
