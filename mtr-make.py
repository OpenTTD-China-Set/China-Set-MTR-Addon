import os, sys, re, subprocess, glob, hashlib

with open("chinaset-mtraddon.pnml","r",encoding='utf-8') as f:
    files_content = f.read()
    file_list = re.findall(r'#include\s+"([^"]+)"', files_content, re.MULTILINE)


with open("chinaset-mtraddon.nml","w",encoding='utf-8') as f:
    for file_name in file_list:
        with open(file_name,"r",encoding='utf-8') as g:
            files_content = g.read()
        f.write(files_content)
        f.write("\n")



result = subprocess.run("nmlc chinaset-mtraddon.nml", shell=True, capture_output=True, text=True)
print(result.stdout)