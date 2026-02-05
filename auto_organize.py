import os
import shutil
import argparse

FOLDERS = {
    "Docs": [".pdf", ".txt", ".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Code": [".py", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar", ".7z"]
}

def get_folder(extension):
    for folder, exts in FOLDERS.items():
        if extension.lower() in exts:
            return folder
    return "Others"

def organize(source_dir, dest_dir, mode="copy"):
    os.makedirs(dest_dir, exist_ok=True)

    for file in os.listdir(source_dir):
        path = os.path.join(source_dir, file)

        if not os.path.isfile(path):
            continue

        _, ext = os.path.splitext(file)
        folder = get_folder(ext)

        target_folder = os.path.join(dest_dir, folder)
        os.makedirs(target_folder, exist_ok=True)

        target_path = os.path.join(target_folder, file)

        if mode == "move":
            shutil.move(path, target_path)
        else:
            shutil.copy(path, target_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-organize a folder by file type.")
    parser.add_argument("source", help="Source folder to organize")
    parser.add_argument("dest", help="Destination folder (organized output)")
    parser.add_argument("--mode", choices=["copy", "move"], default="copy", help="Copy or move files")

    args = parser.parse_args()

    organize(args.source, args.dest, args.mode)
    print("Done. Folder organized.")
