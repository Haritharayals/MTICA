def printBlue():
    print('you choose Blue!\n')
    return
def printRed():
    print('you choose Red!\n')
def printOrange():
    print('you choose Orange!\n')
def printYellow():
    print('you choose Yellow!\n')
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return
colorselect={0:printBlue,1:printRed,2:printOrange,3:printYellow}
selection=0
while True:
    if selection==4:break
    choice()
    selection=int(input("select a color option:"))
    if(selection>=0) and (selection<4):
                  colorselect[selection]()
