import json
inf="""{"Name":"ktrn", "lastName":"sm","Age":12}""" # bu 3 tırnak gerekmekte. içerisinde iblgi olan yapıları json a çevirerek kullanabiliyoruz.
#print(inf["Name"])
read_the_info=json.loads(inf)
print(type(inf))

print(read_the_info["Name"])


import json
with open("C:/Users/Şebnem/Desktoppython further/Jason.txt","r",encoding="utf-8") as Folder:
    turn=json.load(Folder)
    print(turn)