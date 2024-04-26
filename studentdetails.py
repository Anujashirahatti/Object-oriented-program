class Student:
    def __init__(self, name=" ", roll_no=[], marks1=[], marks2=[]):
        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2
    
    # Calculate the result of student
    def calculate_result(self):
        total_marks = self.marks1 + self.marks2
        return total_marks

# Create student objects
student1 = Student(name="anuja", roll_no=5, marks1=90, marks2=92)
student2 = Student(name="raju", roll_no=10, marks1=68, marks2=98)
student3 = Student(name="teju", roll_no=20, marks1=23, marks2=10)
student4 = Student(name="palli", roll_no=5, marks1=86, marks2=95)
student5 = Student(name="varshi", roll_no=30, marks1=88, marks2=90)

enter = input("Enter the student no.: ")
if enter == "student1":
    print(student1.name, student1.roll_no, student1.marks1, student1.marks2)
    student1.calculate_result()
    if student1.calculate_result() >= 35:
        print("Pass")
    else:
        print("Fail")
elif enter == "student2":
    print(student2.name, student2.roll_no, student2.marks1, student2.marks2)
    student2.calculate_result()
    if student2.calculate_result() >= 35:
        print("Pass")
    else:
        print("Fail")
elif enter == "student3":
    print(student3.name, student3.roll_no, student3.marks1, student3.marks2)
    student3.calculate_result()
    if student3.calculate_result() >= 35:
        print("Pass")
    else:
        print("Fail")
elif enter == "student4":
    print(student4.name, student4.roll_no, student4.marks1, student4.marks2)
    student4.calculate_result()
    if student4.calculate_result() >= 35:
        print("Pass")
    else:
        print("Fail")
elif enter == "student5":
    print(student5.name, student5.roll_no, student5.marks1, student5.marks2)
    student5.calculate_result()
    if student5.calculate_result() >= 35:
        print("Pass")
    else:
        print("Fail")
else:
    print("Student not found")




  





     
        