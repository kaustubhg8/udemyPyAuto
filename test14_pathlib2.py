from pathlib import Path

root_dir = Path('files')

file_paths = root_dir.iterdir()

print(Path.cwd())

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_file = path.with_name(new_filename)
    path.rename(new_file)

