import re

UDI_PATTERN = re.compile(
    r"^prismata\.(core|sdk|corp)\.[a-z0-9-]+\.[a-z0-9-]+$"
)

def validate_udi(cmf: dict, repo_scope: str) -> None:
    udi = cmf.get("udi")
    if not isinstance(udi, str):
        raise ValueError("UDI must be a string")

    if not UDI_PATTERN.match(udi):
        raise ValueError(f"UDI '{udi}' does not match canonical pattern")

    scope = udi.split(".")[1]
    if scope != repo_scope:
        raise ValueError(f"UDI scope '{scope}' does not match repo '{repo_scope}'")

    kind_segment = udi.split(".")[2]
    if kind_segment != cmf.get("kind"):
        raise ValueError(
            f"UDI kind segment '{kind_segment}' does not match CMF.kind '{cmf.get('kind')}'"
        )
