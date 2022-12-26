def count_spchar(s):
    spchar=0
    temp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoparstuvwxyz0123456789'
    for i in s:
        if i not in temp:
            spchar+=1
    return  spchar
str1=input()
a=count_spchar(str1)
print("no of special charcater in:",str," ' is",a)
