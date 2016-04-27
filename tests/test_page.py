from django.test import RequestFactory

from building_blocks.pages import DetailPage

from testapp.models import MemberSimple

member = MemberSimple()
member.first_name = "Bill"
member.last_name = "Gates"

factory = RequestFactory()


class MockDetailPage(DetailPage):
    def get_object(self, queryset=None):
        return member


def test_detail_page_view_init():
    DetailPage.as_url(model=member)


def test_detail_page_view_dummy_request():
    url = MockDetailPage.as_url(model=member)
    result = url.callback(factory.get("/31"), pk="31").render()
    assert all(map(lambda x: x in result.content, ["First name", "Bill", "Last name", "Gates"]))
