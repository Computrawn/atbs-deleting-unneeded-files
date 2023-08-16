#!/usr/bin/env python3
# deleting_unneeded_files.py — An exercise in organizing files.
# For more information, see README.md

import logging
import os
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def validate_path() -> Path:
    while True:
        user_path = Path.home() / input("Please type path to directory here: ")
        if not user_path.is_dir():
            print("Directory does not exist.")
            continue
        return user_path


def get_max_file_size() -> int:
    megs_size = input("Please type file size limit in megabytes: ")
    return int(megs_size) * 1000000


def find_large_files(directory: Path, size: int) -> list[Path]:
    """Finds large file sizes in specified directory."""
    large_files = []
    for directory, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = f"{directory}/{filename}"
            file_size = os.path.getsize(file_path)
            if file_size >= size:
                large_files.append(Path(file_path))
    sorted_files = sorted(large_files)
    print("Found the following large files:")
    for filename in sorted_files:
        print(f"* {filename.name} in {filename.parent}")
    return sorted_files


def main():
    valid_path = validate_path()
    max_file_size = get_max_file_size()
    find_large_files(valid_path, max_file_size)


if __name__ == "__main__":
    main()
