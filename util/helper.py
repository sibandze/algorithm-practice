import pathlib
import re

directory = pathlib.Path("~/storage/downloads").expanduser()

for file in directory.glob("*algo-*.pdf"):
    new_filename = re.sub(r'^.*(algo-)', r'algo-', file.name)
    file.rename(file.parent / new_filename)
    print(f"Renamed {file.name} to {new_filename}")
