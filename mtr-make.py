import os, sys, re, subprocess, glob, hashlib, csv

with open("chinaset-mtraddon.pnml","r",encoding='utf-8') as f:
    files_content = f.read()
    file_list = re.findall(r'#include\s+"([^"]+)"', files_content, re.MULTILINE)


with open("chinaset-mtraddon.nml","w",encoding='utf-8') as f:
    for file_name in file_list:
        with open(file_name,"r",encoding='utf-8') as g:
            files_content = g.read()
        f.write(files_content)
        f.write("\n")

def get_vox_hash(vox_path):
    hasher = hashlib.md5()
    with open(vox_path, 'rb') as vox:
        for chunk in iter(lambda: vox.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_gfx_hash_path(gfx_path):
    gfx_hash_path = re.search(r'(.+\\)([^\\]+)(?=\.[^\\]+$)', gfx_path).group(0)
    return gfx_hash_path
def get_palette_path(gfx_path):
    gfx_palette_path = re.search(r'(.+\\)', gfx_path).group(0)
    return gfx_palette_path

search_pattern = os.path.join("gfx/", f'**/*.vox')
gfx_list = glob.glob(search_pattern, recursive=True)
print(gfx_list)
for gfx in gfx_list:            #读取hash并比较
    gfx_hash_path = get_gfx_hash_path(gfx)
    gfx_palette_path = get_palette_path(gfx)
    try:
        with open(".gfxhash\\" + gfx_hash_path,"r",encoding='utf-8') as g:
            vox_hash = g.read()
            vox_real_hash = get_vox_hash(gfx)
            if vox_hash == vox_real_hash:
                pass
            else:
                #os.remove(gfx_hash_path +"_32bpp.png") 
                result = subprocess.run("renderobject -i "+ gfx +" -m manifest.json -overwrite -palette "+ gfx_palette_path +"ttd_palette.json", shell=True, capture_output=True, text=True)
                print(result.stdout, "render ", gfx)
        with open(gfx_hash_path +"_32bpp.png") as h:
            pass
        """ print(gfx_hash_path +"_32bpp.png") """
    except FileNotFoundError:                # 目标文件不存在时的处理
        print(f"E: file:", gfx_hash_path," not be found")
        result = subprocess.run("renderobject -i "+ gfx +" -m manifest.json -overwrite -palette "+ gfx_palette_path +"ttd_palette.json", shell=True, capture_output=True, text=True)
        #print(gfx_palette_path +"ttd_palette.json")
        print(result.stdout, "render ", gfx)
    except Exception as e:
        print(f"E: {e}")


for gfx in gfx_list:        #每次运行后生成新的hash表
    gfx_hash_path = get_gfx_hash_path(gfx)
    """ print(gfx_hash_path) """
    parent_directory = os.path.dirname(".gfxhash\\" + gfx_hash_path)
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory) 
    with open(".gfxhash\\" + gfx_hash_path,"w",encoding='utf-8') as f:
        f.write(get_vox_hash(gfx))

#lng文件生成
strs = []

with open('docs/str.csv', mode='r', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        strs.append(row)
        print(row)

if not os.path.exists("lang/"):
        os.makedirs("lang/") 
with open("lang/english.lng", 'w', encoding='utf-8') as f:
    f.write("##grflangid 0x01"+"\n")
    for i in range(len(strs)):
        if strs[i][1] == "":
            f.write(strs[i][0]+"\n")
        else:
            f.write(strs[i][0]+"   :"+strs[i][1]+"\n")

def other_lang_generate(lang_name, lang_row, lang_code):
    with open("lang/"+lang_name+".lng", 'w', encoding='utf-8') as f:
        f.write("##grflangid "+lang_code+"\n")
        for i in range(len(strs)):
            if strs[i][lang_row] == "":
                if strs[i][1] == "":
                    f.write(strs[i][0]+"\n")
                else:
                    pass
            else:
                f.write(strs[i][0]+"   :"+strs[i][lang_row]+"\n")
   
other_lang_generate("simplified_chinese", 2, "0x56")
other_lang_generate("traditional_chinese", 3, "0x0c")

#编译
result = subprocess.run("nmlc chinaset-mtraddon.nml", shell=True, capture_output=True, text=True)
print(result.stderr)
print(result.stdout)

input("Press Enter to close")