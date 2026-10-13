from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SourceInfo:
    path: str
    repo: str
    imported_at: str

@dataclass
class MetadataInfo:
    name: str
    description: Optional[str]
    tags: List[str]

@dataclass
class RelationsInfo:
    depends_on: List[str]
    provides: List[str]
    conflicts_with: List[str]

@dataclass
class ValidationInfo:
    schema: str
    status: str
    errors: List[str]

@dataclass
class PSO:
    id: str
    udi: str
    kind: str
    version: str
    tenant: Optional[str]
    source: SourceInfo
    metadata: MetadataInfo
    content: dict
    relations: RelationsInfo
    validation: ValidationInfo
    notes: List[str]

def pso_from_cmf(cmf: dict) -> PSO:
    # assume cmf_envelope_validator + udi_validator already run
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
