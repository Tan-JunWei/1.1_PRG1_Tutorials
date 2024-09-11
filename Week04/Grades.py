#Student Name: Tan Jun Wei
#Student ID: S10266704C

marks = float(input("Please enter your marks: "))
if marks >= 85:
    grade = "A+"
    Remark = "Excellent!"
elif marks >= 80:
    grade = "A"
    Remark = "Well done."
elif marks >= 75:
    grade = "B+"
    Remark =""
elif marks >= 70:
    grade = "B"
    Remark =""
elif marks >= 65:
    grade = "C+"
    Remark =""
elif marks >= 60:
    grade = "C"
    Remark =""
elif marks >= 55:
    grade = "D+"
    Remark =""
elif marks >= 50:
    grade = "D"
    Remark = ""
else:
    grade = "F"
    Remark = "See me."
    
print(f"Grade: {grade}\n"
      f"{Remark}")