from pathlib import Path

"""
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""

EXTENSIONS_MAPPING = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
    ".pptx": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".exe": "Programs"
}

DIR = Path('D:/User/Downloads')

files = [f for f in DIR.iterdir() if f.is_file()]
# print(files)
for f in files:
    output_dir = DIR / EXTENSIONS_MAPPING.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)