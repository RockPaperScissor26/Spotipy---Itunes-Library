import os
import shutil

k = input("Spotify Playlist URL: ")
os.system('cmd /c "spotdl [' + k + '] "')
sourcetree = os.path.realpath(__file__)
j = sourcetree
sourcetree = sourcetree.split(r'\ '.replace(" ", ""))
sourcetree = j.replace((sourcetree[-1]), "")
print(sourcetree)
# sourcetree = r'C:\Users\ratth\PycharmProjects\pythonProject\output\Spotify playlist Integration'
print(sourcetree)
if j == "not found":
    #return index -1
    print("song not found")
sourcefile = os.listdir(sourcetree)
#destination = f"{os.environ['UserProfile']}/Desktop/Downloaded Songs"
destination = f"{os.environ['UserProfile']}/Music/iTunes/iTunes Media/Automatically Add to iTunes"
# IF ERROR First, update your install pip install -U spotdl then update youtube-dl pip install -U youtube-dl.

for file in sourcefile:
    print(file)
    if '.mp3' in file:
        shutil.move(os.path.join(sourcetree, file), os.path.join(destination, file))
