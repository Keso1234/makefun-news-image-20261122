"""Copy the news poster to the output directory.

The poster (entry.png) sits beside this file in the repository. This program
copies it, byte for byte, to /output/entry.png (or to the directory named by
MAKEFUN_OUTPUT_DIR, when set, for local runs). Standard library only, no
network, no randomness: both runs write the same bytes.
"""

import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"
MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"poster image not found: {SOURCE}")
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError(
            f"poster image too large: {len(data)} bytes (max {MAX_BYTES})"
        )
    if not data.startswith(PNG_MAGIC):
        raise ValueError("poster image is not a PNG file")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(data)


if __name__ == "__main__":
    main()
