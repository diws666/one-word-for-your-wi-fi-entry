#!/usr/bin/env python3
"""Wi-Fi word entry: writes one word describing Wi-Fi to /output/entry.txt."""

import os

WORD = "ghosting"  # 8 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
