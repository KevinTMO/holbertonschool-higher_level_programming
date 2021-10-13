#!/usr/bin/python3
"""
Module 7-add_item

Method: (No method)

This module will use two functions already created:
- save_to_json_file
- load_from_json_file

Pseudo:

- Import other modules to use (save, load and sys for args)
- Since there's no method, lets use try/except to validate
- Lets use try if there's a file and except if there's not to create a new one
- If there's a file, lets deserialize calling load_from_json_file
- If there's not any file, lets create one calling save_to_json_file
- In try we will just check if there's some content and the file already exist
- In except we will give [] before creating a file to a variable.
- Then, we will call save so we can serialize some object into json file
- When calling save method, we need to concatenate the fileContent and the first
... argument after the filename
"""


from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


File = "add_item.json"

try:
    fileContent = load_from_json_file(File)
except FileNotFoundError:
    fileContent = []

save_to_json_file(fileContent + argv[1:], File)
