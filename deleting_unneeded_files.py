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
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def validate_path() -> Path:
    user_path = Path.home() / input("Please type path to directory here: ")
    if not user_path.is_dir():
        print("Directory does not exist.")
        exit()
    return user_path


def find_large_files(directory):
    """Finds large file sizes in specified directory."""
    large_files = []
    user_size = input("Please type file size limit in megabytes: ")
    bytes_size = int(user_size) * 1000000
    for directory, _, filenames in os.walk(directory):
        directory_size = 0
        for filename in filenames:
            file_path = f"{directory}/{filename}"
            file_size = os.path.getsize(file_path)
            directory_size += file_size
            if file_size >= bytes_size:
                large_files.append(f"{file_path}")

    print(f"The following files exceed the limit of {user_size} MB:")
    for filename in large_files:
        filename = filename.split("/")
        print(f"* {filename[-1]}")


def main():
    valid_path = validate_path()
    find_large_files(valid_path)


if __name__ == "__main__":
    main()
