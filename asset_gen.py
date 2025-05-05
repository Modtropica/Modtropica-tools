import os
import json

# this is where poptropica is stored
base_path = r"..\..\game_data\pop_data\content"

# replace this with the island you what to replace
data_path = R"www.poptropica.com\game\assets\scenes\example"

full_base_path = os.path.join(base_path, data_path)

# replace this with your folder in your mod
replacement_base = "asset"

directories = [name for name in os.listdir(full_base_path) if os.path.isdir(os.path.join(full_base_path, name))]
file_data = {"file_Datas": []}

def scan_directory(directory, base_prefix, replacement_prefix, data_path):
    """ Recursively scans a directory and processes files. """
    for root, _, files in os.walk(directory):
        for filename in files:
            relative_path = os.path.relpath(os.path.join(root, filename), base_prefix)
            file_path = os.path.join(data_path, relative_path).replace("\\", "/")
            replacement_path = os.path.join(replacement_prefix, relative_path).replace("\\", "/")
            if os.path.exists(replacement_path):
                print(f"added {replacement_path}")
                file_data["file_Datas"].append({
                    "type": 3,
                    "file_name": file_path,
                    "file_replacement_name": replacement_path
                })

# Loop through directories and scan recursively
for directory in directories:
    full_dir_path = os.path.join(full_base_path, directory)
    if os.path.exists(full_dir_path) and os.path.isdir(full_dir_path):
        scan_directory(full_dir_path, full_base_path, replacement_base, data_path)

# uh
json_output_path = "patch/asset.json"

# Write JSON output to file
with open(json_output_path, "w", encoding="utf-8") as json_file:
    json.dump(file_data, json_file, indent=4)

print(f"JSON data written to {json_output_path}")