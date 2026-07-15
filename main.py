import json

try:
   with open("Students.json","r")as file:
      students = json.load(file)
except:
   students = []

def save_data():
   with open("Students.json","w")as file:
      json.dump(students,file,indent=4)
      
def add_student():
    name = input("Enter student name : ")
    rollno = int(input("Enter roll no : "))
    for student in students:
       if rollno == student["Roll No"]:
          print("Roll Number already exists!")
          return
    print(" Student Added Successfully!" "\n Name : ",name )
    print(" Roll No : ",rollno)
   
    print("\nSubject Hindi :-")
    marks1=int(input("Enter your marks :"))
    print("\nSubject Math :-")
    marks2=int(input("Enter your marks : "))
    print("\nSubject English :-")
    marks3=int(input("Enter your marks : "))
    total_marks = marks1 + marks2 + marks3 
    print( "Total marks : ",marks1 + marks2 + marks3)
    average = (marks1 + marks2 + marks3)/3
    print("Average : " ,(marks1 + marks2 + marks3)/3)
    if 100 >= average >= 80:
        print("Grade A")
        grade = "A"
    elif 79 >= average >= 60:
        print("Grade B")
        grade = "B"
    elif 59 >= average >= 45:
        print("Grade C")
        grade = "C"
    else:
        print("Grade D")  
        grade = "D" 
    
    print("\nStudent Details : ")

    student = {
        "Name" : name,
        "Roll No" : rollno,
        "Total marks" : total_marks,
        "Average" : average,
        "Grade" : grade
    } 
    print(student)
    students.append(student)
    save_data()
    print("Student Added Successfully!")

def view_student():
    if len(students) == 0:
      print("No students found!")
    else:
       for student in students:
          print("\n-----Student-----")
          print("Name : ",student["Name"])
          print("Roll No : ",student["Roll No"])
          print("Total marks : ",student["Total marks"])
          print("Average : ",student["Average"])
          print("Grade : ",student["Grade"])

def search_student():
   search_name = input("Enter Student name : ")
   found = False
   for student in students:
     if search_name == student["Name"]:
       print("Name : ",student["Name"])
       print("Roll No : ",student["Roll No"])
       print("Total marks : ",student["Total marks"])
       print("Average : ",student["Average"])
       print("Grade : ",student["Grade"])
       found = True
   if found == False:
     print("Studen not found!")

def update_student():
   roll_no = int(input("Enter Roll No : "))
   for student in students :
        if roll_no == student["Roll No"]:
           marks_1 = {
              "Hindi" : int(input("Enter yours marks : ")),
              "Math" : int(input("Enter your marks : ")),
              "English" : int(input("Enter your marks : "))

           }
           print(marks_1)
           updated_total = marks_1["Hindi"] + marks_1["Math"] + marks_1["English"]
           print("Total marks : ",updated_total)
           updated_average = (marks_1["Hindi"] + marks_1["Math"] + marks_1["English"])/3
           print("Average : ", updated_average)
           updated_grade = " "
           save_data()
           
   if 100 >=  updated_average >= 80:
        updated_grade= "A"
   elif 79 >=  updated_average >= 60:
        updated_grade = "B"
   elif 59 >=  updated_average >= 45:
        updated_grade = "C"
   else: 
        updated_grade = "D" 

        student["Total marks"] = updated_total
        student["Average"] = updated_average
        student["Grade"] = updated_grade

        save_data()
        print("Student Updated Successfully")

def delete_student():
   updated_roll = int(input("Enter your Roll No : "))
   found1 = False
   for student in students:
      if updated_roll  == student["Roll No"]:
        found1 = True
        confirm = input("Are you sure you want to delete this student? (Y/N) : ")
        if confirm.lower() == "y":
         students.remove(student)
         save_data()
         print("Student Deleted Successfully")
        else:
           print("Deletion Cancelled")
   if found1 == False:
       print("Student not found!")

def show_topper():
   if  len(students) == 0:
      print("No students found!")
      return
   
   topper = students[0]
   for student in students:
     if student["Average"] > topper["Average"] :
      topper = student
   print("Topper Details")
   print("Name : ",topper["Name"])
   print("Roll No :", topper["Roll No"])
   print("Total marks :",topper["Total marks"])
   print("Average :",topper["Average"])
   print("Grade :",topper["Grade"])


print("===== Student Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Students")
print("4. Update Marks")
print("5. Delete Student")
print("6. Topper")
print("7. Exit")
while True:
 print("\nMenu :-")

 choice = input("Enter your Choice : ")
 # Add Student
 if choice == "1":
   add_student()
 # View Student
 elif choice == "2":
    view_student()
 # Search Student
 elif choice == "3":
    search_student()
 # Update Student
 elif choice == "4":
     update_student()
 # Delete Student
 elif choice == "5":
    delete_student()
 # Show Topper
 elif choice == "6":
    show_topper()
 # Exit Program
 elif choice == "7":
    print("Thank you for using Student Management System!")
    break
 
 else:
   print("Invalid Choice")