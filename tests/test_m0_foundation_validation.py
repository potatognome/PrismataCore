import os
import sys
from pathlib import Path

import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PrismataCore.validators.cmf_envelope_validator import validate_cmf_envelope
from PrismataCore.validators.udi_validator import validate_udi
from PrismataCore.validators.canonical_schema_validator import validate_canonical_schema
from PrismataCore.validators.relations_validator import validate_relations
from PrismataCore.validators.pso_constructor_validator import pso_from_cmf
from PrismataCore.validators.pso_validator import validate_pso


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIRS = (
    ROOT / "canonical" / "core.schemas",
    ROOT / "canonical" / "object.schemas",
)


def load_canonical_schemas():
    paths = sorted(path for directory in SCHEMA_DIRS for path in directory.glob("*.yaml"))
    return {path: yaml.safe_load(path.read_text(encoding="utf-8")) for path in paths}


def test_m0_foundation_validation():
    schemas = load_canonical_schemas()
    known_udis = {cmf["udi"] for cmf in schemas.values()}

    assert len(schemas) == 13

    for path, cmf in schemas.items():
        validate_cmf_envelope(cmf)
        validate_udi(cmf, "core")
        validate_canonical_schema(cmf)
        validate_relations(cmf, known_udis)

        pso = pso_from_cmf(cmf)
        validate_pso(pso)
        assert pso.tenant is None
        assert pso.udi == cmf["udi"]
        print(f"ok: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    failures = 0
    try:
        test_m0_foundation_validation()
    except Exception as exc:
        failures += 1
        print(f"FAIL: test_m0_foundation_validation: {exc}")
    sys.exit(failures)
