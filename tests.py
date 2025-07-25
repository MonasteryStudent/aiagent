# tests.py

# import unittest
from functions.get_files_info import get_files_info

# class TestFunction(unittest.TestCase):
#     def test_current_dir(self):
#         result = get_files_info("calculator")
#         # write manually the expected result of the get_fiels_info function
#         expected = "" 
#         self.assertEqual(result, expected)

def main():
    test_dirs = [".", "pkg", "/bin", "../"]

    for i in range(len(test_dirs)):
        if test_dirs[i] == ".":
            print("Result for current directory:")
        else:
            print(f"Result for '{test_dirs[i]}' directory:")
        print(get_files_info("calculator", test_dirs[i]))
        # if i < len(test_dirs) - 1:
        #     print()

if __name__ == "__main__":
    main()