





#my_list=[1,2,3,"fariborz",4,5,"chakavak","narin","sadaf","narin"]




#my_list.append(400)

#res=my_list.copy()
#
#my_list[0]="chakavak"
#print(res)
#print("*"*30)
#print(my_list)
#print("$"*30)


#res=my_list.count("narin")
#print(res)
#my_list2=["goli","sara","lili"]
#my_list.extend(my_list2)
#print(my_list)


#my_list=[1,2,3,"fariborz",4,5,"chakavak","alireza","sadaf","narin","farnaz","mozhi","maryam"]
#print(len(my_list))
#res=my_list.index("narin",8,14)
#print(res)

#my_list.insert(4,"mona")
#print(my_list)

#res=my_list.pop(7)
#print(res)
#print("*"*30)
#print(my_list)

#my_list.remove("alireza")
#my_list.remove("alireza")
#print(my_list)

#mylist=[1,2,5,10,700,20,3,4,9,10,17]
#mylist.sort(reverse=True)
#print(mylist)
#mylist.clear()
#print(mylist)
#mylist.reverse()
#mylist.
#print(mylist)





#str->itr ,sequnece ,immutable
#name="fariborz ekhtiari"
#print(name[0])
#for i in name:
#    print(i)
#name[0]="t"
#
#print(name)


#res=name.capitalize()

#res=name.index("r",3)
#name="FARIBORZ"

#res=name.count("i")
#res=name.casefold()
#name="FARIBORZ"
#name="fariborz"
#res=name.lower()
#res=name.encode()
#res=name.endswith("borz")
#res=name.expandtabs(4)
#res=name.find("i",4)
#f="ek"
#res=name.join()
#print(res)

#res=name.partition("i")
#f="ekhtiari"
#res=name.maketrans()
#print(name)
#res=name.lstrip()
#res=name.removeprefix("hello_")
#res=name.removesuffix("fariborz")
#res=name.replace("r","R",count=1)
#res=name.rindex("r")
#print(res)
#print("*"*30)
#res2=name.index("r")
#print(res2)

#name="فریبرز"
#res=name.split("r")
#res=name.swapcase()

#res=name.title()
#res=name.upper()

#res=name.isalnum()
#res=name.isascii()
#res=name.isalpha()
#res=name.isidentifier()
#name=" "
#res=name.isspace()
#print(res)



#name="chaKavk"
#
#res=name.isprintable()
#print(res)


#name=input("esm:")
#
#print(f"hello{name:+>10.2}jan")


from os import system

while True:
    name=input("esmet:").capitalize()
    if name=="" or name.isspace()==True:
        system("cls")
        print("oskol khodeti esmet?")
        
        continue
    else:
        if name.isalpha()==True and name.isdigit()!=True:
            print("name ok ")