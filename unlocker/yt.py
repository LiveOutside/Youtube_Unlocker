from os.path import abspath


def add_gbdpi_conf(gbdpi_path: str) -> str:
    """
    Writes Youtube config for GBDPI to unlock CIS speed limit
    """
    x86_64_path = abspath(gbdpi_path + "/x86_64/")
    try:
        with open(abspath(x86_64_path + "/youtube-domain.txt"), "w") as conf:
            conf.write("googlevideo.com")
        print(": Successfuly created GBDPI config for Youtube")
        return x86_64_path
    except Exception as e:
        print(f"!! Error while writing GBDPI config for Youtube: {e}")
