import os, sys, re, subprocess, glob, hashlib

def get_vox_hash(vox_path):
    hasher = hashlib.md5()
    with open(vox_path, 'rb') as vox:
        for chunk in iter(lambda: vox.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_gfx_hash_path(gfx_path):
    gfx_hash_path = ".gfxhash\\" + re.search(r'(.+\\)([^\\]+)(?=\.[^\\]+$)', gfx_path).group(0)
    return gfx_hash_path

search_pattern = os.path.join("gfx/", f'**/*.vox')
gfx_list = glob.glob(search_pattern, recursive=True)
print(gfx_list)
for gfx in gfx_list:            #读取hash并比较
    gfx_hash_path = get_gfx_hash_path(gfx)
    try:
        with open(gfx_hash_path,"r",encoding='utf-8') as g:
            vox_hash = g.read()
            vox_real_hash = get_vox_hash(gfx)
            if vox_hash == vox_real_hash:
                pass
            else:
                result = subprocess.run("renderobject -i "+ gfx, shell=True, capture_output=True, text=True)
                print(result.stdout)
        with open(gfx_hash_path +"_32bpp.png") as h:
            pass
    except FileNotFoundError:                # 目标文件不存在
        print(f"E: file:", gfx," not be found")
        result = subprocess.run("renderobject -i "+ gfx, shell=True, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"E: {e}")



for gfx in gfx_list:
    gfx_hash_path = get_gfx_hash_path(gfx)
    """ print(gfx_hash_path) """
    parent_directory = os.path.dirname(gfx_hash_path)
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory) 
    with open(gfx_hash_path,"w",encoding='utf-8') as f:
        f.write(get_vox_hash(gfx))


