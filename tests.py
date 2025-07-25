# tests.py

from functions.get_files_info import get_files_info

def main():
    test_dirs = [".", "pkg", "/bin", "../"]

    for i in range(len(test_dirs)):
        if test_dirs[i] == ".":
            print("Result for current directory:")
        else:
            print(f"Result for '{test_dirs[i]}' directory:")
        print(get_files_info("calculator", test_dirs[i]))

if __name__ == "__main__":
    main()