from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
path = "/home/elabz/Documents/Books"

for x in os.listdir(path):
    y = drive.CreateFile({title: x})
    y.SetContentFile(os.path.join(path, x))
    y.Upload()
    y = None
