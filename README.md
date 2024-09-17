
# File Organization Script

This script organizes files in a specified directory into subdirectories based on their file types. The file types are determined by their extensions, and the script moves each file into a corresponding subdirectory.

## Features

- Organizes files into subdirectories based on their file extensions.
- Creates new subdirectories for each file type if they don't already exist.
- Supports a customizable mapping of file extensions to file types.

## Requirements

- Python 3.x
- `os` module (standard library)
- `shutil` module (standard library)

## Usage

1. **Clone the repository** (if applicable) or download the script file.

2. **Edit the script**:
   - Modify the `FILE_TYPE_MAP` dictionary to include any additional file extensions and their corresponding file types as needed.
   - Replace `'C:/Users/Admin/Downloads'` with the path to the directory you want to organize.

3. **Run the script**:
   ```bash
   python script_name.py
   ```

## How It Works

1. The script defines a mapping of file extensions to file types in the `FILE_TYPE_MAP` dictionary.
2. The `organize_files_by_type` function iterates through all files in the specified directory.
3. For each file, the script determines the file type based on its extension.
4. The script creates a new subdirectory for the file type if it doesn't already exist.
5. The script moves the file into the corresponding subdirectory.

## Notes

- Ensure that the directory path provided is correct and accessible.
- The script only processes files and ignores directories within the specified directory.
