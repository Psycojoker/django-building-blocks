from django.test import RequestFactory

from building_blocks.page_views import DetailPageView

from testapp.models import MemberSimple

member = MemberSimple()
member.first_name = "Bill"
member.last_name = "Gates"

factory = RequestFactory()


class MockDetailPageView(DetailPageView):
    def get_object(self, queryset=None):
        return member


def test_detail_page_view_init():
    DetailPageView.as_view(model=member)


def test_detail_page_view_dummy_request():
    view = MockDetailPageView.as_view(model=member)
    result = view(factory.get("/31"), pk="31").render()
    assert all(map(lambda x: x in result.content, ["First name", "Bill", "Last name", "Gates"]))
