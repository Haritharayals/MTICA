import sys
print("coming through stdoubt")
save_stdout=sys.stdout
fh=open(r"d:\mtica\\test.txt","w")
sys.studout=fh
print("This line goes to test.txt")
print(input())
sys.stdout=save_stdout
fh.close()
                 
