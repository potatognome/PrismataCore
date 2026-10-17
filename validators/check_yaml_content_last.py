import os
import re
import sys
from pathlib import Path

# Determine PrismataCore root relative to this script (two levels up when placed in validators)
ROOT = Path(__file__).resolve().parents[1]

yaml_files = list(ROOT.rglob('*.yaml')) + list(ROOT.rglob('*.yml'))
print(f'Found {len(yaml_files)} YAML files under {ROOT}\n')

try:
    import yaml
    have_py_yaml = True
except Exception:
    have_py_yaml = False

key_line_re = re.compile(r'^([A-Za-z0-9_-]+):\s*(#.*)?$')

errors = []
reports = []
for p in yaml_files:
    rel = p.relative_to(ROOT)
    try:
        data = p.read_text(encoding='utf-8')
    except Exception as e:
        errors.append((str(rel), 'read_error', str(e)))
        continue
    report = {'file': str(rel), 'parsed': None, 'content_last': None, 'parse_error': None}
    # attempt parse
    if have_py_yaml:
        try:
            yaml.safe_load(data)
            report['parsed'] = True
        except Exception as e:
            report['parsed'] = False
            report['parse_error'] = str(e)
            errors.append((str(rel), 'parse_error', str(e)))
    else:
        report['parsed'] = 'pyyaml_missing'

    # find top-level keys in order
    top_keys = []
    for ln in data.splitlines():
        if not ln.strip():
            continue
        if ln.startswith(' ') or ln.startswith('\t'):
            continue
        m = key_line_re.match(ln)
        if m:
            key = m.group(1)
            top_keys.append(key)
    if top_keys:
        last_key = top_keys[-1]
        report['content_last'] = (last_key == 'content')
        if not report['content_last']:
            errors.append((str(rel), 'content_not_last', last_key))
    else:
        report['content_last'] = 'no_top_keys'
        errors.append((str(rel), 'no_top_level_keys', ''))

    reports.append(report)

# Summarize
print('Summary report:')
ok_count = sum(1 for r in reports if r['content_last'] is True and (r['parsed'] in (True, 'pyyaml_missing')))
print(f'  OK files (content last & parsed or parser missing): {ok_count}')
print(f'  Total files checked: {len(reports)}')
if errors:
    print('\nIssues found:')
    for f, kind, info in errors:
        print(f' - {f}: {kind} ({info})')
    sys.exit(1)
else:
    print('\nNo issues found.')
    sys.exit(0)
