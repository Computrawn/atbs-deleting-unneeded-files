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
    """Prompt user until valid path given. Return valid path object."""

    while True:
        user_path = Path.home() / input("Please type path to directory here: ")
        if not user_path.is_dir():
            print("Directory does not exist. Try again.")
            continue

        return user_path


def get_file_size_limit() -> int:
    "Prompt user for file size limit in MB and returns bytes size integer."

    return int(input("Please type file size limit in megabytes: ")) * 1000000


def detect_large_files(directory: Path, size: int) -> list[Path]:
    """Search directory and its subdirectories for files of size specified
    by user, then prints file details to standard out."""

    large_files = []

    for directory, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = Path(f"{directory}/{filename}")
            file_size = file_path.stat().st_size
            if file_size >= size:
                large_files.append(file_path)
    sorted_files = sorted(large_files)

    if sorted_files:
        print("Found the following large files:")
        for filename in sorted_files:
            print(f"* {filename.name} in {filename.parent}")
    else:
        print(f"No files greater than {int(size // 1000000)} MB found.")

    return sorted_files


def main():
    """Main sequence."""
    valid_path = validate_path()
    file_size_limit = get_file_size_limit()
    detect_large_files(valid_path, file_size_limit)


if __name__ == "__main__":
    main()
