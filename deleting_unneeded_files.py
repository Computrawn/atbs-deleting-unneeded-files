#!/usr/bin/env python3
# deleting_unneeded_files.py — An exercise in organizing files.
# For more information, see README.md

import logging
import os
import send2trash

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def find_size(directory):
    """Finds large file sizes and directories. If the directory exceeds limit, user is prompted
    to examine its contents."""
    large_files = []
    large_dirs = []
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
        if directory_size >= bytes_size:
            large_dirs.append(directory)

    if large_dirs:
        ld = ", ".join(large_dirs)
        print(f"The following folders exceed the size limit: {ld}")
        # print(f"The following files are larger than {size_limit}: {large_files}")
        print("Please examine their contents.")
    else:
        print(f"Nothing above {user_size} megabytes found.")
    print(f"The following files exceed the limit of {user_size} MB:")
    for filename in large_files:
        filename = filename.split("/")
        print(f"* {filename[-1]}")


def main():
    find_size(input("Please type path to directory here: "))


if __name__ == "__main__":
    main()
