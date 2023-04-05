import os
import sys

def add_prefix_to_files(directory, prefix):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and not filename.startswith(prefix):
            new_filename = prefix + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python prefix-my-files.py <directory_path> <prefix>")
        sys.exit(1)

    directory_path = sys.argv[1]
    prefix = sys.argv[2]
    add_prefix_to_files(directory_path, prefix)
