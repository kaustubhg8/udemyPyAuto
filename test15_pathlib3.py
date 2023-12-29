from pathlib import Path

root_dir = Path('files')
file_path = root_dir.glob("**/*")

for path in file_path:
    if path.is_dir():
        for f in path.glob("**/*"):
            parent_folder = f.parts[-2]
            # print(parent_folder)
            new_name = parent_folder + "_" + f.stem + f.suffix
            new_file = f.with_name(new_name)
            f.rename(new_file)