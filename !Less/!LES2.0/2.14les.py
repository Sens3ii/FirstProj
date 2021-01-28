import os
import fnmatch
# os.mkdir("4")
# os.makedirs("Hello")
# with os.scandir("C:\Pyth") as entries:
#     for entry in entries:
#         if fnmatch.fnmatch(entry.name,'*.txt'):
#             print(entry.name)
with os.scandir("C:\Pyth") as items:
    for item in items:
        if item.is_file():
            if fnmatch.fnmatch(item.name,"*.py"):
                print(f"------{item.name}")
                file = open(item.name)
                content = file.read()
                print(content)
                file.close()