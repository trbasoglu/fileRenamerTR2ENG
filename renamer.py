from glob import glob
import os

def renameFile(oldname):
    oldname = oldname.replace('ı','i')
    oldname = oldname.replace('İ','I')
    oldname = oldname.replace('ü','u')
    oldname = oldname.replace('Ü','U')
    oldname = oldname.replace('ğ','g')
    oldname = oldname.replace('Ğ','G')
    oldname = oldname.replace('ş','s')
    oldname = oldname.replace('Ş','S')
    oldname = oldname.replace('ç','c')
    oldname = oldname.replace('Ç','C')
    oldname = oldname.replace('ö','o')
    oldname = oldname.replace('Ö','O')
    return oldname


files = glob("*");
for filename in files:
    print(f"{filename}==>{renameFile(filename)}")
    os.rename(filename,renameFile(filename))
