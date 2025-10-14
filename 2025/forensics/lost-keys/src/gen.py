import os
import random
import string
from random import randrange

# CONFIGURATION
BASE_DIR = "./test"
NUM_FOLDERS = 1000
FILES_PER_FOLDER = 55
MAX_DEPTH = 7
FILE_EXTENSIONS = ['.txt', '.log', '.data', '.bin', '.dat']

RECOVERY_KEY = "187308-501424-128810-520894-548779-314006-451924-201729"

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def random_folder(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_random_directory_tree(base_dir, num_folders, max_depth):
    created_folders = set()

    for _ in range(num_folders):
        depth = random.randint(1, max_depth)
        parts = [random_folder(6) for _ in range(depth)]
        path = os.path.join(base_dir, *parts)
        os.makedirs(path, exist_ok=True)
        created_folders.add(path)

    return list(created_folders)

def create_random_file(folder_path, ctr):
    file_name = random_folder(8) + random.choice(FILE_EXTENSIONS)
    file_path = os.path.join(folder_path, file_name)

    if ctr == 998:
        with open(file_path, 'w') as f:
            f.write(RECOVERY_KEY)
        print(f"Recovery key: {file_path}")
    else:
        with open(file_path, 'w') as f:
            f.write(random_string(randrange(10, 100)))

    # print(f"Created: {file_path}")

def main():
    ctr = 0
    all_folders = create_random_directory_tree(BASE_DIR, NUM_FOLDERS, MAX_DEPTH)

    # Walk through all subfolders and drop files in each
    for root, dirs, _ in os.walk(BASE_DIR):
        for _ in range(random.randint(1, FILES_PER_FOLDER)):
            create_random_file(root, ctr)
            ctr = ctr + 1

if __name__ == "__main__":
    main()