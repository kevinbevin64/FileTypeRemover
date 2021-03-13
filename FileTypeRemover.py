import sys
import os
from os import listdir

dir_name = input("Targetted file location - ")
test = os.listdir(dir_name)

ext1 = input("What file type do you want to remove ('.zip')  - ")

for item in test:
    if item.endswith(ext1):
        os.remove(os.path.join(dir_name, item))
