#! python3
"""deleting_unneeded_files.py — An exercise in organizing files.
For more information, see enclosed project_details.txt file."""

import os
import send2trash

large_files = []


def find_size(user_dir):
    for dir_name, subfolders, filenames in os.walk(user_dir):
        for filename in filenames:
            dir_path = f"{dir_name}/{filename}"
            file_size = os.path.getsize(dir_path)
            if file_size >= 100_000_000:
                large_files.append(f"{dir_path}: {file_size}")
    print(large_files)


dir_path = input("Please type path to directory here: ")
find_size(dir_path)
