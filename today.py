import os
import sys
from datetime import datetime

def create_folder_structure(folder_name):
    base_path = os.getcwd()
    target_dir = os.path.join(base_path, folder_name)

    # Files to create inside the target directory
    files = {
        "description.md": "# Description\n",
        f"{folder_name}.py": "",  # Empty Python file
        "schema.py" if "nth" in folder_name else "pandas_schema.py": "# Schema definition\n"
    }

    # Create target directory
    os.makedirs(target_dir, exist_ok=True)

    # Create each file only if it doesn't already exist
    for filename, content in files.items():
        file_path = os.path.join(target_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created: {file_path}")
        else:
            print(f"Skipped (already exists): {file_path}")

    print(f"Folder checked/created at: {target_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python today.py <folder-name>")
        sys.exit(1)

    folder_name = sys.argv[1]
    create_folder_structure(folder_name)
