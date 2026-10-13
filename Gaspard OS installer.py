import requests
from pathlib import Path
url = "https://api.github.com/repos/Gasrobot73/Gaspard-OS/contents/Gaspard%20OS"
dossier = Path.home() / ".Gaspard OS"
def telecharger(url, chemin):
    chemin.mkdir(parents=True, exist_ok=True)
    for f in requests.get(url).json():
        if f["type"] == "dir":
            telecharger(f["url"], chemin / f["name"])
        elif f["type"] == "file":
            r = requests.get(f["download_url"])
            r.raise_for_status()
            (chemin / f["name"]).write_bytes(r.content)
telecharger(url, dossier)
print("Téléchargement terminé !")
from pathlib import Path
import win32com.client
from win32com.shell import shell, shellcon
exe = Path.home() / ".Gaspard OS" / "Gaspard OS.exe"
bureau = Path(
    shell.SHGetFolderPath(
        0,
        shellcon.CSIDL_DESKTOPDIRECTORY,
        None,
        0
    )
)
shell = win32com.client.Dispatch("WScript.Shell")
raccourci = shell.CreateShortCut(
    str(bureau / "Gaspard OS.lnk")
)
raccourci.TargetPath = str(exe)
raccourci.save()
#ça telecharge le repo mais pas le raccourci