from pathlib import Path
import re

def print_keys(p):
    key_line_re = re.compile(r'^([A-Za-z0-9_-]+):\s*(#.*)?$')
    s = Path(p).read_text(encoding='utf-8')
    lines = s.splitlines()
    keys = []
    for ln in lines:
        if not ln.strip():
            continue
        if ln.startswith(' ') or ln.startswith('\t'):
            continue
        m = key_line_re.match(ln)
        if m:
            keys.append(m.group(1))
    print('File:', p)
    print('---')
    print(s)
    print('--- top keys:', keys)

print_keys('PrismataCore/tests/fixtures/invalid_cmf_missing_fields.yaml')
print('\n')
print_keys('PrismataCore/examples/registry/border-role.d/default.border-role.entry.yaml')
