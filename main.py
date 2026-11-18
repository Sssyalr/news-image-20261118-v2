#!/usr/bin/env python3
"""Copy the entry image into the make.fun output directory.

Reads the entry image (entry.png, next to this script) and writes it to
MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png). Standard library
only, deterministic: the output bytes are exactly the input bytes.
"""

import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / ENTRY_NAME
    if not source.is_file():
        print(f"error: {ENTRY_NAME} not found next to {__file__}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / ENTRY_NAME

    shutil.copyfile(source, dest)

    # Verify the copy is complete: output must be byte-identical to the input.
    if dest.stat().st_size != source.stat().st_size:
        print(
            f"error: size mismatch after copy "
            f"({source.stat().st_size} -> {dest.stat().st_size})",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {dest} ({dest.stat().st_size} bytes, verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
