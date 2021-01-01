
#student report card

roll_no = input("please enter roll no : ")
name = str(input("please enter name : "))
total = 0;

subjects = {"english": 0, "telugu" : 0 , "hindi": 0, "maths": 0, "science" : 0, "social": 0}
for subs in subjects:
    subjects[subs] = int(input("please enter " + subs +" marks : "))
    total = total + subjects[subs]


avg = total/6

# print(str(roll_no)+","+str(name)+"," +str(total)+"," +str(avg)+"," , end = "")
print('roll no:',roll_no, ',', 'name:',name, ',', 'total:', total, ',', 'avg:',avg, ',', 'grade:', end = "")
if avg < 40:
    print("Promoted ")
elif avg < 50:
    print("D")
elif avg < 60:
    print("C")
elif avg < 80:
    print("B")
elif avg <= 100:
    print("A")