from django.test import RequestFactory

from building_blocks.pages import DetailPage
from building_blocks.page_groups import CRUD

from testapp.models import MemberSimple

member = MemberSimple()
member.first_name = "Bill"
member.last_name = "Gates"

factory = RequestFactory()


class MockDetailPage(DetailPage):
    def get_object(self, queryset=None):
        return member

CRUD.DetailPage = MockDetailPage


def test_detail_crud_dummy_request():
    urls = CRUD.as_urls(model=member)
    result = urls[0].callback(factory.get("/31"), pk="31").render()
    assert all(map(lambda x: x in result.content, ["First name", "Bill", "Last name", "Gates"]))
