#!/usr/bin/env python3
"""Run every test_*.py in this directory as an independent script and summarize results.

This runner executes each test file as a subprocess using the same Python
interpreter, captures exit codes, and prints a concise summary. It is safe to
run from the repository or from within the `tests` directory.
"""

from pathlib import Path
import subprocess
import sys


def run_all():
    root = Path(__file__).parent
    test_files = sorted([p for p in root.glob('test_*.py') if p.name != Path(__file__).name])
    total = len(test_files)
    failures = 0
    results = []

    for p in test_files:
        print(f"Running {p.name}...")
        proc = subprocess.run([sys.executable, str(p)], cwd=str(root))
        ok = proc.returncode == 0
        results.append((p.name, ok, proc.returncode))
        if not ok:
            failures += 1

    print("\nSummary:")
    for name, ok, rc in results:
        print(f"{name}: {'OK' if ok else 'FAIL'} (exit {rc})")

    print(f"\nTotal: {total}, Passed: {total - failures}, Failed: {failures}")
    sys.exit(0 if failures == 0 else 1)


if __name__ == '__main__':
    run_all()
