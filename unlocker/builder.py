from unlocker.loader import *
from unlocker.static.config import EXTRACTION_DIR
from unlocker.yt import add_gbdpi_conf
from unlocker.autorun_setup import *
from os.path import abspath


def build_gbdpi() -> str:
    """
    Builds GBDPI
    """
    download_gbdpi()
    time.sleep(10)
    archived_gbdpi_path = get_gbdpi_dir()
    extracted_gbdpi_path = unpack_gbdpi(archived_gbdpi_path, EXTRACTION_DIR)
    x86_64_path = add_gbdpi_conf(extracted_gbdpi_path)
    return x86_64_path


def build_batch(x86_64_path: str) -> None:
    """
    Builds .bat file and adds it to autorun (if perms)
    """
    batch_name = "yt_unlocker.bat"
    batch_path = abspath(x86_64_path + "/" + batch_name)
    try:
        with open(batch_path, "w+") as yt_bat:
            yt_bat.write(f"""@echo off
cd /d {x86_64_path}
goodbyedpi.exe --blacklist youtube-domain.txt -6
""")
        print(": Batch build successful <3")
        add_to_startup(batch_name, batch_path)

    except Exception as e:
        print(f"!! Error while building batch file: {e}")
