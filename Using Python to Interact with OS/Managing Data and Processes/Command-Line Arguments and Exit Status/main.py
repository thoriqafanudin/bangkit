import os
import sys

print(sys.argv)

file_name = sys.argv[1]

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("New file created\n")
else:
    print(f"Error, the file {file_name} already exists")
    sys.exit(1)