
def revthestring(s):
    rs = list(s)
    l = len(s)-1
    for i in range(0, (len(s)-1)//2):
        temp = rs[i]
        rs[i] = s[l-i]
        rs[l-i] = temp
    str1 = "".join(rs)
    return str1


string = input('Enter the string : ')
print('The un-inverted string is : ', end=" ")
print(string)
print('The inverted string is : ', end=" ")
print(revthestring(string))
