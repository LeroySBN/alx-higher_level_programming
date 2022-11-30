#!/usr/bin/python3
def remove_char_at(str, n):
    strord = []
    newstr = ""

    if (n > len(str)) or (n < 0):
        pstr = "{}".format(str)
    else:
        for i in range(len(str)):
            strord.append(ord(str[i]))
        strord.pop(n)

        for j in range(len(strord)):
            newstr += chr(strord[j])
        pstr = "{}".format(newstr)
    return pstr
