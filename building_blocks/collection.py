from building_blocks.base import Model
from building_blocks.url import to_url


class Collection:
    def to_urls(self):
        return list(map(to_url, self.views.values()))

    def decorate(self, decorators):
        # example CRUD(Post).decorate(Haml)
        if not isinstance(decorators, (list, tuple)):
            decorators = [decorators]

        for name, view in self.views.items():
            for decorator in decorators:
                self.views[name] = decorator(view)


class CRUD(Collection):
    # assuming ordered dict
    views = {
        "list_view": None,
        "create_view": None,
        "update_view": None,
        "delete_view": None,
        "read_view": Model,
    }

    def __init__(self, model, decorators=None):
        super(CRUD, self).__init__(decorators=decorators)
        self.model = model
        self.views = {name: view(model) for name, view in self.views.items()}


class CollectionOfCollection:
    collections = []

    def to_urls(self):
        urlpatterns = []

        for collection in collections:
            urlpatterns += collection.to_url()

        return urlpatterns
