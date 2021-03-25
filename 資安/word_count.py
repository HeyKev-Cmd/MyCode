f = open("./text.txt", "r")
list={}

for text in f.readlines():
    text=text.replace(" ","")
    for i in text:
        if (i not in list):
            list[i]=1
        elif (i in list):
            list[i]+=1
            pass
            
     
for i in list:
    print(i,":",list[i],"\n")

