import os
s = os.getcwd()
os.walk(s,topdown = true)
for dir, dirs, files in os.walk(s):
    print(f'Found directory {dir}')
    for file in files:
        print(file)
