import re, csv, os

strs = []

with open('docs/str.csv', mode='r', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        strs.append(row)
        print(row)


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