import os
import sys

def create_archive(files):
    for file_name in files:
        with open(file_name, 'rb') as f: #binary read mode
            file_data = f.read()
            file_size = len(file_data) #getting size of file
            sys.stdout.buffer.write(file_name.encode() + b'\n') #writing file name
            sys.stdout.buffer.write(str(file_size).encode() + b'\n') #writing file size
            sys.stdout.buffer.write(file_data)

def extract_archive(): #for file extracting
    while True: #until there are no more lines
        file_name = sys.stdin.buffer.readline().strip()
        if not file_name:
            break
        file_size = int(sys.stdin.buffer.readline().strip()) #size
        file_data = sys.stdin.buffer.read(file_size) #binary data
        with open(file_name.decode(), 'wb') as f: #writing data to new file
            f.write(file_data)

def main():
    if len(sys.argv) < 2:
        print("no args... exit") # if no arguments are passed exit program
        sys.exit(1)

    mode = sys.argv[1]

    if mode == 'c': #archive file
        if len(sys.argv) < 3:
            print("No file found")
            sys.exit(1)
        files = sys.argv[2:]
        create_archive(files)

    elif mode == 'x': #extract the archive file
        extract_archive()

if __name__ == '__main__':
    main()
