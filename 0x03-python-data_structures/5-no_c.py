#!/usr/bin/python3
def no_c(my_string):
    my_string2 = ""
    for i in range(len(my_string)):
        if (my_string[i] == "c"):
            continue
        elif (my_string[i] == "C"):
            continue
        else:
            my_string2 += my_string[i]
    return my_string2
