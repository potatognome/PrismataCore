"""
PrismataCore — PSO Loader

Loads a CMF capsule, validates it using the Core validator suite,
and produces a deterministic PSO runtime object.

This module performs:
1. CMF envelope validation
2. UDI validation
3. Canonical schema validation (if kind == schema)
4. Relations validation
5. CMF → PSO conversion
"""

import yaml
from typing import Dict, Set

from .cmf_envelope_validator import validate_cmf_envelope
from .udi_validator import validate_udi
from .canonical_schema_validator import validate_canonical_schema
from .relations_validator import validate_relations

from PrismataCore.pso.pso import pso_from_cmf


# ------------------------------------------------------------
# Load CMF YAML file
# ------------------------------------------------------------

def load_cmf_file(path: str) -> Dict:
    """Load a CMF YAML file from disk."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ------------------------------------------------------------
# Full CMF → PSO pipeline
# ------------------------------------------------------------

def load_pso(
    path: str,
    repo_scope: str,
    known_udis: Set[str]
):
    """
    Load a CMF file, validate it, and convert it into a PSO.

    Parameters:
        path: filesystem path to CMF YAML file
        repo_scope: "core", "sdk", or "corp"
        known_udis: set of all valid UDI strings in this repo

    Returns:
        PSO object
    """

    cmf = load_cmf_file(path)

    # 1. Envelope validation
    validate_cmf_envelope(cmf)

    # 2. UDI validation
    validate_udi(cmf, repo_scope)

    # 3. Canonical schema validation (only for schema objects)
    if cmf["kind"] == "schema":
        validate_canonical_schema(cmf)

    # 4. Relations validation
    validate_relations(cmf, known_udis)

    # 5. Convert CMF → PSO
    return pso_from_cmf(cmf)
