import os
from config import MAX_FILE_SIZE


def get_file_content(working_directory, file_path):
    # if file_path is a relative path outside the working_directory, join returns the file_path
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path_working_dir = os.path.abspath(working_directory)
    print(target_path)
    print(abs_path_working_dir)
    if not target_path.startswith(abs_path_working_dir):
        return f'Error: Cannot read "{target_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{target_path}"'
    try:
        with open(target_path, "r") as f:
            print(os.path.getsize(target_path))
            if os.path.getsize(target_path) > MAX_FILE_SIZE:
                file_content_string = f.read(MAX_FILE_SIZE)
                file_content_string += f'...File "{target_path}" truncatedat {MAX_FILE_SIZE} characters'
            else:
                file_content_string = f.read()
        return file_content_string
    except Exception as e:
        return f'Error reading file: {e}'

def test():
    files_content = get_file_content("calculator", "lorem.txt")
    print(files_content)
    
if __name__ == "__main__":
    test()
