import os

def rename_files(directory, prefix):
    """Renames all files in the given directory with the provided prefix."""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_name = f"{prefix}_{filename}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print(f"Files in {directory} renamed with prefix '{prefix}'")

if __name__ == "__main__":
    rename_files(r'D:\ipc_sas', 'backup')
