def validate_canonical_schema(cmf: dict) -> None:
    if cmf["kind"] != "schema":
        return  # only enforce for schemas

    content = cmf["content"]
    if not isinstance(content, dict):
        raise ValueError("Schema content must be an object")

    # basic canonical rules
    required = ["fields", "required"]
    for f in required:
        if f not in content:
            raise ValueError(f"Schema.content missing required field '{f}'")

    if not isinstance(content["fields"], dict):
        raise ValueError("Schema.content.fields must be an object")

    if not isinstance(content["required"], list):
        raise ValueError("Schema.content.required must be a list")
