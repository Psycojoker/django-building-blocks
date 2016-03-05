from building_blocks.components import DetailComponent

from testapp.models import MemberSimple
from .utils import django_test_utils


member = MemberSimple()
member.first_name = "Bill"
member.last_name = "Gates"


def test_detail_component_init():
    DetailComponent(model=member)


def test_detail_component_fields():
    fields = list(DetailComponent(model=member).fields())

    expected_fields = [
        {"name": "First name", "value": "Bill"},
        {"name": "Last name", "value": "Gates"},
    ]

    assert fields == expected_fields


def test_detail_component_render():
    html = DetailComponent(model=member).render()

    expected_result = "\n".join((
        '<h2>%s</h2>' % member,
        '<p><b>First name</b>: Bill</p>',
        '<p><b>Last name</b>: Gates</p>',
    ))

    django_test_utils.assertHTMLEqual(html, expected_result)
