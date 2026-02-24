# File Organization Automation (Python)

Automatically organize mixed folders into clean, share-ready structures (Docs, Images, Code, Archives, Others).

## Overview

This service classifies files by extension and copies or moves them into category folders for faster delivery and review.

## Visual Schema

```text
+-----------------------------+
| Input Folder (Unorganized)  |
+-----------------------------+
              |
              v
+-----------------------------+
| auto_organize.py            |
| mode: copy or move          |
+-----------------------------+
              |
              v
+-----------------------------+
| File Type Classification    |
| Docs / Images / Code / etc. |
+-----------------------------+
              |
              v
+-----------------------------+
| Clean Output Folder         |
+-----------------------------+
```

## Requirements

- Python 3.8+

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Quickstart

```bash
python auto_organize.py "input_folder" "output_folder" --mode copy
```

- `--mode copy` keeps original files
- `--mode move` moves files to destination

## Input

- Source folder path (first positional argument)
- Destination folder path (second positional argument)
- Optional transfer mode (`--mode copy` or `--mode move`)

## Output

- Destination folder with grouped subfolders (`Docs`, `Images`, `Code`, `Archives`, `Others`)
- Files ready for client review, packaging, or archiving

## Example

### Before

![Before](example_before.png)

### After

![After](example_after.png)

## Use Cases

- Rapid cleanup of mixed delivery folders
- Preparing handoff-ready folder structures
- Reducing repetitive manual sorting effort

## Notes

- The script processes only the source folder top level (`os.listdir`) and does not recurse into subfolders.
- If a target filename already exists, copy/move follows default `shutil` behavior for that platform/path.

## License

MIT License. See `LICENSE`.
