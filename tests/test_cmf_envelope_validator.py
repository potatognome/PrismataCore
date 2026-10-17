import os
import sys
import yaml

# Ensure project root is on sys.path so imports work when running as script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PrismataCore.validators.cmf_envelope_validator import validate_cmf_envelope


FIXTURES = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_valid_cmf():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "valid_cmf.yaml")))
    validate_cmf_envelope(cmf)


def test_invalid_cmf_missing_fields():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "invalid_cmf_missing_fields.yaml")))
    try:
        validate_cmf_envelope(cmf)
        assert False, "Expected failure"
    except ValueError:
        assert True


if __name__ == "__main__":
    # Simple test runner for script execution
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
