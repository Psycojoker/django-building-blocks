from building_blocks.components import DetailComponent
from building_blocks.fields import Field

from testapp.models import MemberSimple
from .utils import django_test_utils


member = MemberSimple()
member.first_name = "Bill"
member.last_name = "Gates"


def test_detail_component_init():
    DetailComponent(model=member)


def test_detail_component_fields():
    def fields_are_equal(a, b):
        for i, j in zip(a, b):
            if not i.field == j.field and i.model == j.model:
                return False

        return True

    fields = list(DetailComponent(model=member).fields())

    expected_fields = [
        Field(member._meta.fields[1], member),
        Field(member._meta.fields[2], member),
    ]

    assert fields_are_equal(fields, expected_fields)


def test_detail_component_render():
    html = DetailComponent(model=member).render()

    expected_result = "\n".join((
        '<h2>%s</h2>' % member,
        '<p><b>First name</b>: Bill</p>',
        '<p><b>Last name</b>: Gates</p>',
    ))

    django_test_utils.assertHTMLEqual(html, expected_result)
