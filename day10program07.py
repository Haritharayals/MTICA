fo1=open(r"C:\PythonPractice18\day10.txt","r")
fo2=open(r"C:\PythonPractice18\day10a.txt","w+")
temp=fo1.read()
fo2.write(temp)


fo1.close()
fo2.close()
print("file copied")
