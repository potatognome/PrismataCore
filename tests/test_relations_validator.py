import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PrismataCore.validators.relations_validator import validate_relations


FIXTURES = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_relations_invalid_udi():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "relations_invalid_udi.yaml")))
    known = {"prismata.core.schema.pane"}  # only pane exists

    try:
        validate_relations(cmf, known)
        assert False
    except ValueError:
        assert True


if __name__ == "__main__":
    failures = 0
    for name, obj in list(globals().items()):
        if name.startswith("test_") and callable(obj):
            try:
                obj()
                print(f"ok: {name}")
            except Exception as e:
                failures += 1
                print(f"FAIL: {name}: {e}")
    sys.exit(failures)
