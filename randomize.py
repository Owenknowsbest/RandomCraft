import os
import shutil
import random
folders = {"block","colormap","effect","environment","gui","item","map","misc","mob_effect","models/armor","painting","particle","font"}
def randomize(t):
    filelist=os.listdir('textures/'+t)
    for fichier in filelist[:]:
        if not(fichier.endswith(".png")):
            filelist.remove(fichier)
    names = filelist
    for file in filelist:
        r = random.randint(0,len(names)-1)
        shutil.copy('textures/'+t+'/'+file,'assets/minecraft/textures/'+t+'/'+names[r])
        names.remove(names[r])
for t in folders:
    randomize(t)