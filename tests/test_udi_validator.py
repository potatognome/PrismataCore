import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PrismataCore.validators.udi_validator import validate_udi


FIXTURES = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_valid_udi():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "valid_cmf.yaml")))
    validate_udi(cmf, "core")


def test_invalid_udi():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "invalid_udi.yaml")))
    try:
        validate_udi(cmf, "core")
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
