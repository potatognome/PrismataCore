import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from PrismataCore.validators.pso_constructor_validator import pso_from_cmf
from PrismataCore.validators.pso_validator import validate_pso


FIXTURES = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_pso_validator():
    cmf = yaml.safe_load(open(os.path.join(FIXTURES, "valid_cmf.yaml")))
    pso = pso_from_cmf(cmf)
    validate_pso(pso)


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
