"""
PrismataCore — PSO Validator

Validates a PSO runtime object after CMF → PSO conversion.
Ensures the PSO envelope is structurally correct and deterministic.

This validator does NOT validate schema content.
It only validates the PSO envelope.
"""

from PrismataCore.pso.pso import PSO


def validate_pso(pso: PSO) -> None:
    """
    Validate structural correctness of a PSO object.

    Assumes CMF validators have already run.
    This is a runtime safety check.
    """

    # Basic type checks
    if not isinstance(pso.id, str):
        raise ValueError("PSO.id must be a string")

    if not isinstance(pso.udi, str):
        raise ValueError("PSO.udi must be a string")

    if not isinstance(pso.kind, str):
        raise ValueError("PSO.kind must be a string")

    if not isinstance(pso.version, str):
        raise ValueError("PSO.version must be a string")

    # Tenant may be None or string
    if pso.tenant is not None and not isinstance(pso.tenant, str):
        raise ValueError("PSO.tenant must be None or a string")

    # SourceInfo
    src = pso.source
    if not isinstance(src.path, str):
        raise ValueError("PSO.source.path must be a string")
    if not isinstance(src.repo, str):
        raise ValueError("PSO.source.repo must be a string")
    if not isinstance(src.imported_at, str):
        raise ValueError("PSO.source.imported_at must be a string")

    # MetadataInfo
    meta = pso.metadata
    if not isinstance(meta.name, str):
        raise ValueError("PSO.metadata.name must be a string")
    if meta.description is not None and not isinstance(meta.description, str):
        raise ValueError("PSO.metadata.description must be None or a string")
    if not isinstance(meta.tags, list):
        raise ValueError("PSO.metadata.tags must be a list")

    # Content (schema‑agnostic)
    if not isinstance(pso.content, dict):
        raise ValueError("PSO.content must be a dict")

    # RelationsInfo
    rel = pso.relations
    for field in ("depends_on", "provides", "conflicts_with"):
        lst = getattr(rel, field)
        if not isinstance(lst, list):
            raise ValueError(f"PSO.relations.{field} must be a list")
        for udi in lst:
            if not isinstance(udi, str):
                raise ValueError(f"PSO.relations.{field} entries must be UDI strings")

    # ValidationInfo
    val = pso.validation
    if not isinstance(val.schema, str):
        raise ValueError("PSO.validation.schema must be a string")
    if not isinstance(val.status, str):
        raise ValueError("PSO.validation.status must be a string")
    if not isinstance(val.errors, list):
        raise ValueError("PSO.validation.errors must be a list")

    # Notes
    if not isinstance(pso.notes, list):
        raise ValueError("PSO.notes must be a list")
