import os
import sys
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PrismataCore.validators.pso_loader import load_pso


FIXTURES = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_pso_loader():
    known = {"prismata.core.schema.pane"}
    pso = load_pso(
        os.path.join(FIXTURES, "valid_cmf.yaml"),
        repo_scope="core",
        known_udis=known
    )
    assert pso.udi == "prismata.core.schema.pane"


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
