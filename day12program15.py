class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print('name:'+self.name.title()+'\nRoll.no: '\
              +str(self.rollno))
        print('college: '+self.college+'\nCourses: '+self.course)
lstObj=[]
for i in range(2):
    n=input()
    r=int(input())
    temp='obj'+str(i)
    temp=Student(n,r)
    lstObj.append(temp)
for i in lstObj:
    i.displayStudent()
