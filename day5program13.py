def extract_digits(s):
    extract_digits=0
    for i in s:
        if i in '0123456789':
            extract_digits+=1
    return extract_digits
str1=input()
a=extract_digits(str1)
print("no of digits in:",str1," ' is",a)
