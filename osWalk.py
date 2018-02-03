import os


def main():
    root_dir = "D:" + os.sep + "PHP" + os.sep + "VM" + os.sep + "tensorflow"
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)


if __name__ == '__main__':
    main()
