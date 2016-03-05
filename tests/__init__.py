import sys
from importd import d

sys.path.append("..")

d(INSTALLED_APPS=["tests.testapp", "building_blocks"])
