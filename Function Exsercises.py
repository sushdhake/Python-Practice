def gradeCalc(hscore,ascore,escore):
    final = (hscore + ascore + escore) / 175 * 100
    return round(final,2)



name = input("please enter the students name:")

hscore = int(input("please enter the homework score:"))
while hscore > 25:
    print("Invalid number,try again")
    hscore = int(input("please enter the homework score"))


ascore = int(input("please enter the assessment score:"))
while ascore >50:
    print("Invalid number,try again")
    ascore = int(input("please enter the homework score"))
    
escore = int(input("please enetr the exam score:"))
while escore > 100:
    print("Invalid number,try again")
    escore = int(input("please enter the homework score:"))


result = gradeCalc(hscore, ascore, escore)

if result >= 80:
    grade = "A"
elif result >= 70:
    grade = "8"
elif result >= 60:
    grade = "c" 
else:
    grade = "F"           

print(f"{name} scored:{gradeCalc(hscore,ascore,escore)} ")