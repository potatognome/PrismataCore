def validate_relations(cmf: dict, known_udis: set[str]) -> None:
    rel = cmf["relations"]

    for field in ("depends_on", "provides", "conflicts_with"):
        if field not in rel:
            raise ValueError(f"relations.{field} missing")
        if not isinstance(rel[field], list):
            raise ValueError(f"relations.{field} must be a list")

        for udi in rel[field]:
            if not isinstance(udi, str):
                raise ValueError(f"relations.{field} entry must be a string UDI")
            if udi not in known_udis:
                # you can choose: warn vs error; here we error
                raise ValueError(f"relations.{field} references unknown UDI '{udi}'")
