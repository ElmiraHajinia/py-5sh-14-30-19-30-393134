

""" 
سیستم مدیریت نمرات دانشجویان
:اطلاعات دانشجویان و نمراتشان را با کدملی ذخیره کن. قابلیت‌ها
ثبت دانشجوی جدید
حذف دانشجو
تغییر نمره
محاسبه میانگین کلاس
پیدا کردن بالاترین و پایین‌ترین نمره
نمایش دانشجویان قبول و مردود
"""

from student import*
while True:
    command=input("1.add 2.delete 3.edit 4.average 5.max and min grade 6.show 7.passed and failed students 8.exit===")
    match command:
        case "1":
            while True:
                ID_number=input("enter the ID number===")
                if len(ID_number)==10:
                    name=input("enter the name===")
                    family=input("enter the family===")
                    grade=float(input("enter the grade==="))
                    if 0<=grade<=20:
                        information={"name":name,"family":family,"grade":grade}
                        IDDD(ID_number,information)
                        print("added")
                        print(students)
                        break
                    else:
                        print("grade is wrong")
                else:
                    print("ID number is wrong")
        case "2":
            while True:
                delete=input("enter the ID_number")   
                if delete in students:
                    deleteee(delete) 
                    print("deleted") 
                    print(students)
                    break
                else:
                    print("ID number doesn't exist")   
        case "3":
            while True:
                edit=input("enter the ID_number")
                if edit in students:
                    grade=float(input("enter the new grade==="))
                    edittt(edit,grade)
                    print("edited") 
                    print(students)
                    break
                else:
                    print("ID number doesn't exist")
        case "4":
            grades=0
            for information in students.values():
                grades=information["grade"]+grades
   
            average=grades/len(students)  
            print("average=",average)

        case "5":
            all_grades=[]
            for information in students.values():
                all_grades.append(information["grade"])


            minimum_grade=min(all_grades) 
            maximum_grade=max(all_grades) 
            print("minimum_grade=", minimum_grade)  
            print("maximum_grade",maximum_grade)

        case "6":
            print(students)    

        case "7":
            for ID_number,information in students.items():
                print(information["grade"])
                if information["grade"]>=10:
                    print(ID_number, "passed")

                else:
                    print(ID_number, "failed")

        case "8": 
            break           





                

