import os
from struct import pack
from mii2studio import output
from time import sleep

# a lot of code comes from Mii2Studio
# https://github.com/HEYimHeroic/mii2studio/tree/74014fe199a358e809b2af2022a6eafaa7ec9931
# It's a cool project; Check it out!

def echo(x):
    print(x)
    return x

print("Please read the ReadMe first!")

try:
    os.mkdir("files")
except:
    pass
try:
    os.mkdir("files/temp")
except:
    pass
try:
    os.mkdir("output")
except:
    pass
try:
    os.mkdir("output/miigx")
except:
    pass

rkgfiles = os.listdir("files")

first_input = input("Y for Normal \"Read Files from Folder\" mode\nP for \"Paste bytes\" mode\nQ for quit\n >> ").lower()

def isRKG(x:str):
    if x.endswith(".rkg") is True:
        return x
    if x.endswith(".RKG") is True:
        return x

def read_bytes(wbytes):
    if "," in wbytes:
        filenum = 0
        wbytes = wbytes.split(",")
        for x in wbytes:
            with open(f"files/temp{filenum}.miigx","w") as f:
                f.write(x)
            filenum+=1
            output(filenum,f"files/temp{filenum}.miigx")
    else:
        with open(f"files/temp.miigx","w") as f:
            f.write(bytes.fromhex(wbytes).decode(u"utf-16be"))
            output(-1,f"files/temp.miigx")
    return ""    

def read_rkg(rkgfiles):
    rkgfiles = list(filter(isRKG,rkgfiles))
    num = 1
    for x in rkgfiles:
        with open(f"files/{x}","rb") as rf, open(f"files/temp/{num}.miigx","wb") as wf:
            rf.seek(60)
            rkgd = rf.read(74)
            wf.write(rkgd)
        output(f"files/temp/{num}.miigx",num)
        num += 1
    
    os.rename(f"files/temp/{num}.miigx",f"files/temp/{num}.miigx")
    os.rmdir("files/temp")
    sleep(10)
    quit()

# continuation of inputs after the start

match first_input:
    case "y" : 
        read_rkg(rkgfiles)
        quit()
    case "p" :
        print("Paste now.\nPut commas between Miis if you have more than one.")
        inp = input().strip("\n").strip(" ").strip("")
        read_bytes(inp)
        quit()
    case _ : quit()