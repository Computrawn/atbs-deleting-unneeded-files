#! python3
"""deleting_unneeded_files.py — An exercise in organizing files.
For more information, see enclosed project_details.txt file."""

import os
import send2trash

large_files = []
large_dirs = []
size_limit = int(input("Please type file size limit in bytes: "))
dir_path = input("Please type path to directory here: ")


def find_size(user_dir):
    """Finds large file sizes and directories. If the directory exceeds limit, user is prompted
    to examine its contents. If file size exceeds limit, user is given option to keep or
    delete file."""
    for dir_name, subfolders, filenames in os.walk(user_dir):
        dir_size = 0
        for filename in filenames:
            file_path = f"{dir_name}/{filename}"
            file_size = os.path.getsize(file_path)
            dir_size += file_size
            if file_size >= size_limit:
                large_files.append(f"{file_path}")
        if dir_size >= size_limit:
            large_dirs.append(dir_name)

    if large_dirs:
        ld = ", ".join(large_dirs)
        print(f"The following folders exceed the size limit: {ld}")
        print("Please examine their contents.")
    else:
        print("Nothing above size limit found.")

    if large_files:
        for lf in large_files:
            print(f"{lf} exceeds size limit.")
            del_confirm = input(
                "Type del to send it to the trash or keep to retain file. "
            )
            if del_confirm.lower() == "del":
                print(f"\nSending {lf} to trash.\n")
                send2trash.send2trash(lf)
            else:
                print("File will remain in directory.")


find_size(dir_path)
