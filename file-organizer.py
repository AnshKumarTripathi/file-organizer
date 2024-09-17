import os
import shutil

# Define your mapping of file extensions to file types
FILE_TYPE_MAP = {
    'txt': 'Text Files',
    'docx': 'Text Files',
    'png': 'Image Files',
    'jpg': 'Image Files',
    'pdf': 'PDF Files',
    'mp3': 'Music & Videos Files',
    'mp4': 'Music & Videos Files',
    # Add more mappings as needed
}

def organize_files_by_type(directory):
    for filename in os.listdir(directory):
        # Ignore directories, only process files
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the file extension
            file_ext = filename.split('.')[-1]

            # Get the file type from the map, or use 'Other' if the file extension is not in the map
            file_type = FILE_TYPE_MAP.get(file_ext, 'Other')

            # Create a new directory for this file type, if it doesn't exist
            new_dir = os.path.join(directory, file_type)
            os.makedirs(new_dir, exist_ok=True)

            # Move the file into the new directory
            shutil.move(os.path.join(directory, filename), os.path.join(new_dir, filename))

# Usage
organize_files_by_type('C:/Users/Admin/Downloads')

