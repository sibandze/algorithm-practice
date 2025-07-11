import pathlib
import re

directory = pathlib.Path("~/storage/downloads").expanduser()
start = input().strip()  # strip whitespace
if not start:
    return

pattern = rf'^.*({re.escape(start)}.*\.pdf)$'
for file in directory.glob(f"*{start}*.pdf"):
    new_filename = re.sub(pattern, r'\1', file.name)
    if file.name == new_filename:
        print(f"{file.name} already saved properly.")
        continue
    file.rename(file.parent / new_filename)
    print(f"Renamed {file.name} to {new_filename}")
