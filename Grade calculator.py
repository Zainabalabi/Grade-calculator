"""
A=70-100
B=60-69
C=50-59
D=45-49
E=40-44
F=0-39

"""

x= int(input("give a grade:"))

if x>=70 and x<=100:
    print("A \nExcellent")
elif x>=60 and x<=69:
    print("B \nVery good")
elif x>=50 and x<=59:
    print("C \nGood")
elif x>=45 and x<=49:
    print("D \nFair")
elif x>=40 and x<=44:
    print("E \nPass")
elif x>=0 and x<=39:
    print("F \nFail")
    

