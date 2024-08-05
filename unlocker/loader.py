from pathlib import Path
from unlocker.static.config import DOWNLOADS_DIR, GBDPI_RELEASE_URL
from glob import glob
from os.path import basename, abspath
from os import remove
from zipfile import ZipFile
from webbrowser import open as web_open
import time

# # Probably should use pywin32, but it has some compability issues
# downloads_path = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Downloads)

def download_gbdpi() -> None:
    """
    Hardcoded variation of HTTP installation of GBDPI
    """
    web_open(GBDPI_RELEASE_URL, new=1, autoraise=True)


def get_gbdpi_dir() -> str:
    """
    Finds the directory of installed GoodbyeDPI by ValdikSS
    """
    if DOWNLOADS_DIR is None:
        downloads_path = abspath(str(Path.home() / "Downloads"))
    else: 
        downloads_path = DOWNLOADS_DIR
    gbdpi_archived_path = abspath(glob(f"{downloads_path}/goodbyedpi*[-_.0-9]*.zip")[0])

    return gbdpi_archived_path


def unpack_gbdpi(gbdpi_path: str, extract_to: str) -> (str | None):
    """
    Extracts GBDPI to a specified folder
    """
    extract_to = abspath(extract_to)
    try:
        with ZipFile(gbdpi_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
            print(f": Extracted all files: '{extract_to}'")

        remove(gbdpi_path)
        print(f": Created folder path: {extract_to + basename(gbdpi_path).replace(".zip", "")}")
        return extract_to + basename(gbdpi_path).replace(".zip", "")
        
    except Exception as e:
        print(f"!! Error during .zip extraction: {e}")



