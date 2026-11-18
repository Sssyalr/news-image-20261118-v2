#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261118 bounty (v2).

The image this entry submits is built ahead of time: a newspaper-style
infographic summing up the world news of Wednesday 18 November 2026 in
eight stories, from Shenzhen to the Gulf, Kyiv to Kinshasa. It ships in
this repository as entry.png. This program's only job is to place an
exact copy of that image at the path the grader reads.

It uses nothing but the standard library, touches no network, and writes
the same bytes on every run, so the two grading runs agree byte for byte.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    # The grader mounts the repository read-only at /bot, so the image
    # sits next to this file. Resolve it from our own path rather than
    # from the working directory, which the grader does not guarantee.
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    # The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output, the
    # directory the rules name, when the variable is not set.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination = out_dir / "entry.png"

    if not source.is_file():
        print(f"entry.png not found next to {__file__}", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    # A plain copy keeps the bytes identical to the shipped file.
    shutil.copyfile(source, destination)

    # Confirm the copy landed whole before reporting success, so a
    # truncated write is caught here instead of by the grader.
    if destination.stat().st_size != source.stat().st_size:
        print("copied entry.png has the wrong size", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
