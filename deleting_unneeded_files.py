#! python3
"""deleting_unneeded_files.py — An exercise in organizing files.
For more information, see enclosed project_details.txt file."""

import os
import send2trash
import shutil


def find_size(search_dir):
    for dir_name, subfolders, filenames in os.walk(search_dir):
        for filename in filenames:
            dir_path = f"{dir_name}/{filename}"
            file_size = os.path.getsize(dir_path)
            if file_size >= 100_000_000:
                print(f"{dir_path}: {file_size}")


search_dir = input("Please type path to directory here: ")
find_size(search_dir)
