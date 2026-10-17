"""
PrismataCore — PSO (Prismata Schematic Object)

The PSO is the canonical runtime representation of any CMF object.
It is schema‑agnostic, deterministic, and stable across schema evolution.

CMF = storage capsule
PSO = runtime capsule

All PrismataCore validators operate on CMF and PSO envelopes.
All SDK tools consume PSO objects.
Tenants store CMF objects only.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict


# ------------------------------------------------------------
# Envelope Sub‑Objects
# ------------------------------------------------------------

@dataclass
class SourceInfo:
    """Provenance information for CMF objects."""
    path: str
    repo: str
    imported_at: str


@dataclass
class MetadataInfo:
    """Human‑readable metadata for CMF/PSO objects."""
    name: str
    description: Optional[str]
    tags: List[str]


@dataclass
class RelationsInfo:
    """UDI‑based dependency relationships."""
    depends_on: List[str]
    provides: List[str]
    conflicts_with: List[str]


@dataclass
class ValidationInfo:
    """Validation status for CMF/PSO objects."""
    schema: str
    status: str
    errors: List[str]


# ------------------------------------------------------------
# PSO — Prismata Schematic Object
# ------------------------------------------------------------

@dataclass
class PSO:
    """
    Canonical runtime representation of a CMF object.

    All fields mirror the CMF envelope.
    The `content` field is schema‑agnostic and may evolve freely.
    """

    id: str
    udi: str
    kind: str
    version: str
    tenant: Optional[str]

    source: SourceInfo
    metadata: MetadataInfo
    content: Dict
    relations: RelationsInfo
    validation: ValidationInfo
    notes: List[str]


# ------------------------------------------------------------
# CMF → PSO Constructor
# ------------------------------------------------------------

def pso_from_cmf(cmf: Dict) -> PSO:
    """
    Convert a validated CMF capsule into a PSO runtime object.

    Assumes:
    - cmf_envelope_validator has run
    - udi_validator has run
    - canonical_schema_validator has run (if kind == schema)
    - relations_validator has run

    This function performs no validation itself.
    It is a pure, deterministic CMF → PSO transformation.
    """

    src = cmf["source"]
    meta = cmf["metadata"]
    rel = cmf["relations"]
    val = cmf["validation"]

    return PSO(
        id=cmf["id"],
        udi=cmf["udi"],
        kind=cmf["kind"],
        version=cmf["version"],
        tenant=cmf["tenant"],

        source=SourceInfo(
            path=src["path"],
            repo=src["repo"],
            imported_at=src["imported_at"],
        ),

        metadata=MetadataInfo(
            name=meta["name"],
            description=meta.get("description"),
            tags=meta.get("tags", []),
        ),

        content=cmf["content"],

        relations=RelationsInfo(
            depends_on=rel["depends_on"],
            provides=rel["provides"],
            conflicts_with=rel["conflicts_with"],
        ),

        validation=ValidationInfo(
            schema=val["schema"],
            status=val["status"],
            errors=val.get("errors", []),
        ),

        notes=cmf["notes"],
    )
