import os


def check_dir(path) -> None:
    with open("dir_content.txt", "w", encoding="utf-8") as reader:
        for dirpath, dirnames, filenames in os.walk(path):
            reader.write(f"Directory: {dirpath}\n")
            for dirname in dirnames:
                reader.write(f"  Subdirectory: {dirname}\n")
            for filename in filenames:
                reader.write(f"    File: {filename}\n")


def check_directory(path) -> None:
    with open("directory_contents.txt", "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(path):
            f.write(f"Root: {root}\n")
            for dir in dirs:
                f.write(f"Directory: {dir}\n")
            for file in files:
                f.write(f"File: {file}\n")


def check_distinct_types(path) -> None:
    distinct_files = set()

    for root, dirs, files in os.walk(path):
        for file in files:
            distinct_files.add(file.split(".")[-1])

    with open("distinct_types.txt", "w", encoding="utf-8") as f:
        f.write("\nDistinct File Types:\n")
        for file_type in sorted(distinct_files):
            f.write(f"{file_type}\n")


def delete_non_rar_files0(path) -> None:
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            if not file.endswith(".rar"):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))


def delete_non_rar_files(path) -> None:
    with open("deleted_contents.txt", "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                if not file.lower().endswith(".rar") and not file.lower().endswith(
                    ".zip"
                ):
                    f.write(f"Deleted File: {os.path.join(root, file)}\n")
                    os.remove(os.path.join(root, file))
            for dir in dirs:
                try:
                    os.rmdir(os.path.join(root, dir))
                    f.write(f"Deleted Directory: {os.path.join(root, dir)}\n")
                except OSError:
                    pass


PATH = r"D:\Manga\Temporary"

# Example usage
# check_directory(PATH)
# check_dir(PATH)
# check_distinct_types(PATH)

# Example usage
delete_non_rar_files(PATH)
