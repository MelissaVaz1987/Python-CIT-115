sName=input("Enter your name:")

iTest1=int(input("Enter your test 1 score:"))
iTest2=int(input("Enter your test 2 score:"))
iTest3=int(input("Enter your test 3 score:"))
iTest4=int(input("Enter your test 4 score:"))


if intTest1<=0 or intTest2<=0 or intTest3<=0 or intTest4<=0:
print("Test scores must be greater than 0.")
exit()

sGradeDrop=input("Do you want to drop lowest grade?: Y/N")
if sGradeDrop="Y" and sGradeDrop="N":
exit("Enter Y or Nto drop the lowest grade")    

iDivisionFactor = 4
iLowest = 0


if sChoice == "Y":

    iDivisionFactor = 3

    if iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:
        iTest1 = iLowest

    elif iTest2 < iTest3 and iTest2 < iTest4:
        iTest2 = iLowest

    elif iTest3 < iTest4:
        iTest3 = iLowest

    else:
        iLowest = iTest4


fAverage = (iTest1 + iTest2 + iTest3 + iTest4 - iLowest) / iDivisionFactor


sGrade = ""

if fAverage >= 97.0:
    sGrade = "A+"

elif fAverage >= 94.0:
    sGrade = "A"

elif fAverage >= 90.0:
    sGrade = "A-"

elif fAverage >= 87.0:
    sGrade = "B+"

elif fAverage >= 84.0:
    sGrade = "B"

elif fAverage >= 80.0:
    sGrade = "B-"

elif fAverage >= 77.0:
    sGrade = "C+"

elif fAverage >= 74.0:
    sGrade = "C"

elif fAverage >= 70.0:
    sGrade = "C-"

elif fAverage >= 67.0:
    sGrade = "D+"

elif fAverage >= 64.0:
    sGrade = "D"

elif fAverage >= 60.0:
    sGrade = "D-"

else:
    sGrade = "F"


print(f"{sName} test average is: {fAverage:.1f}")
print(f"Letter grade is: {sGrade}")

    
