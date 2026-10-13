REQUIRED_FIELDS = [
    "id", "udi", "kind", "version", "tenant",
    "source", "metadata", "content",
    "relations", "validation", "notes",
]

def validate_cmf_envelope(cmf: dict) -> None:
    missing = [f for f in REQUIRED_FIELDS if f not in cmf]
    if missing:
        raise ValueError(f"CMF envelope missing fields: {missing}")

    if not isinstance(cmf["notes"], list):
        raise ValueError("CMF.notes must be a list")

    if not isinstance(cmf["relations"], dict):
        raise ValueError("CMF.relations must be an object")

    if not isinstance(cmf["metadata"], dict):
        raise ValueError("CMF.metadata must be an object")

    if not isinstance(cmf["source"], dict):
        raise ValueError("CMF.source must be an object")
