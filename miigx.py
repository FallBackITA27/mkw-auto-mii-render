import os
from mii2studio import output
from time import sleep

# a lot of code comes from Mii2Studio
# https://github.com/HEYimHeroic/mii2studio/tree/74014fe199a358e809b2af2022a6eafaa7ec9931
# It's a cool project; Check it out!

def echo(x):
    print(x)
    return x

# I have yet to finish it
print("Please read the ReadMe first!")

#Creates Files folder, a temp folder inside of it, the output folder and the output folder miigx's
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

# chose input
first_input = input("Y for Normal \"Read Files from Folder\" mode\nP for \"Paste bytes\" mode\nQ for quit\n >> ").lower()
# go to line 77

def isRKG(x:str):
    # filter for the /files/ folder.
    if x.endswith(".rkg") is True:
        return x
    if x.endswith(".RKG") is True:
        return x

def read_bytes(wbytes):
    # Currently unfinished.
    quit()
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
    # filters out any non-.rgk file
    rkgfiles = list(filter(isRKG,rkgfiles))
    # num for the file name
    num = 1
    for x in rkgfiles:
        # opens the rkg and writes the miidata in the temp folder
        with open(f"files/{x}","rb") as rf, open(f"files/temp/{num}.miigx","wb") as wf:
            # 0xC3 Offset | 0x4A Length | Blocks 0xC3 to 0x85
            rf.seek(60)
            rkgd = rf.read(74)
            wf.write(rkgd)
        # calls Mii2Studio
        output(f"files/temp/{num}.miigx",num)
        num += 1
    
    # moves the temp file to the completed folder; I wanna move this line on the Mii2Studio.py script and make the file name {mii_name}.miigx 
    os.rename(f"files/temp/{num}.miigx",f"files/temp/{num}.miigx")
    # remove temp dir
    os.rmdir("files/temp")
    sleep(10)
    quit()

# continuation of input after the start

match first_input:
    case "y" :
        second_input = input("Press enter when you put the files in the file folder.")
        # reads the files in the files folder
        rkgfiles = os.listdir("files")
        read_rkg(rkgfiles)
    case "p" :
        print("Paste now.\nPut commas between Miis if you have more than one.")
        inp = input().strip("\n").strip(" ").strip("")
        read_bytes(inp)
        quit()
    case _ : quit()