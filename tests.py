# tests.py

#from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def tests():

    # - get_files_info tests
    # test_dirs = [".", "pkg", "/bin", "../"]

    # for i in range(len(test_dirs)):
    #     if test_dirs[i] == ".":
    #         print("Result for current directory:")
    #     else:
    #         print(f"Result for '{test_dirs[i]}' directory:")
    #     print(get_files_info("calculator", test_dirs[i]))

    # - get_file_content test
    # result = get_file_content("calculator", "small_lorem.txt")
    # print(result)

    # - get_file_content tests
    file_paths = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

    for file_path in file_paths:
        file_content = get_file_content("calculator", file_path)
        print(f"Result for '{file_path}':")
        print(file_content)



if __name__ == "__main__":
    tests()