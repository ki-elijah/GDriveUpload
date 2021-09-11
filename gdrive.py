from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gat = GoogleAuth()
gat.LocalWebServerAuth()

dr = GoogleDrive(gat)
path = "/home/elabz/Documents/Books"

for x in os.listdir(path):
    y = drive.CreateFile({title: x})
    y.SetContentFile(os.path.join(path, x))
    y.Upload()
    y = None
