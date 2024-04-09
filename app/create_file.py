import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(filename: str, content: list[str]) -> None:
    with open(filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        for idx, line in enumerate(content, start=1):
            file.write(f"{idx} {line}\n")


def main() -> None:
    if len(sys.argv) < 3:
        return

    flags = set(sys.argv[1:])
    directory_path = ""
    content = []

    if "-d" in flags:
        try:
            directory_index = sys.argv.index("-d") + 1
            directory_path = os.path.join(*sys.argv[directory_index:])
            create_directory(directory_path)
        except IndexError:
            print("No directory path")
            return

    if "-f" in flags:
        try:
            filename_index = sys.argv.index("-f") + 1
            filename = sys.argv[filename_index]
            print("Enter content line:")
            while True:
                line = input()
                if line.lower() == "stop":
                    break
                content.append(line)
            create_file(os.path.join(directory_path, filename), content)
        except IndexError:
            print("No file name")
            return


if __name__ == "__main__":
    main()
