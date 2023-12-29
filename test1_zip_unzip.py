import shutil
from pathlib import Path

import zipfile

root_dir = Path('files/data')
file_paths = root_dir.glob("*/")
destination_path = Path('files/data')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r')as zf:
        # final_path = destination_path / Path(path.stem)
        zf.extractall(path=destination_path)

for path in file_paths:
    if not path.is_file():
        print(path)
        shutil.rmtree(path)
#         path.rmdir()

