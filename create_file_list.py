from glob import glob
import json

files = glob("problems/*.md")
file_names = []
for file in files:
    file_names.append(file.split("/")[-1])

json.dump(file_names, open("problem_lists.json", "w"))
