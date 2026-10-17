import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PrismataCore.validators.canonical_schema_validator import validate_canonical_schema


FIXTURES = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_valid_schema():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "valid_schema_cmf.yaml")))
    validate_canonical_schema(cmf)


def test_invalid_schema_missing_fields():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "invalid_schema_missing_fields.yaml")))
    try:
        validate_canonical_schema(cmf)
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
