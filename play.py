def mun(x):
    if x < 5:
        if x > 0 and x < 5:
            print "nest"
        elif x > 0 and x < 3:
            print "nest2"
    elif x > 5:
        print "ya man"


is_dad = 8

dict_list = {}
dict_list["cat"] = "is dog"
dict_list["mom"] = is_dad
dict_list["cool"] = 34
dict_list["cake"] = True

print dict_list.values()
