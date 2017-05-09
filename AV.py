import os
import datetime
import random, array

SIGNATURE = "CRANKLIN PYTHON VIRUS"
<<<<<<< HEAD

=======
>>>>>>> origin/master
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == True:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect

filestoinfect = search(os.path.abspath("/home/prong/Documents/ECS189m/project1"))
for fname in filestoinfect:
    print ("kjhkjh")
    print (fname)

	
