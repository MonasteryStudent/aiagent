import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_path_wdir = os.path.abspath(working_directory)
    # If file_path is a relative path outside the working_directory, 
    # os.path.join() returns file_path. If i input "/bin", join() 
    # detects that it is not on path but if i otherwise insert "bin" 
    # join() appends it with a slash.
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_path.startswith(abs_path_wdir):
        return f'Error: Cannot write to "{target_path}" as it is outside the permitted working directory'
    try:
        # os.path.dirname returns the abs path to the directory where the target file is.
        # If this dir doesn't exist os.path.exists returns false. In that case os.makedirs
        # creates the dir and the following open() function can write to the target file.
        # Warning: This overwrites preexisting files!!
        path_to_dir = os.path.dirname(target_path)
        if not os.path.exists(path_to_dir):
            os.makedirs(path_to_dir)
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{target_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)


def test():
    result = write_file("calculator", "lorem_trust_me.txt", "wait, this isn't lorem ipsum")
    print(result)

if __name__ == "__main__":
    test()
