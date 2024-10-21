class Person:

    def __init__(self,id=None,name=None):
        self.id = id
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Student(Person):
    Student_dict = {}
    def __init__(self,id=None,name=None,student_class=None,roll_number=None):
        super().__init__(id,name)
        self.student_class = student_class
        self.roll_number = roll_number

    def get_class(self):
        return self.student_class

    def get_roll_number(self):
        return self.roll_number


class Teacher(Person):
    Teacher_dict = {}
    def __init__(self,id=None,name=None,subject_taught=None,set_password=None):
        super().__init__(id,name)
        self.subject_taught = subject_taught
        self.set_password = set_password

    def get_subject(self):
        return self.subject_taught
    
    def get_password(self):
        return self.set_password


class Attendance(Teacher):
    Attendance_dict = {}

    def mark_attendance(self, student_id, date):
        if date in self.Attendance_dict.keys():
            self.Attendance_dict[date].append(student_id)
        else:
            self.Attendance_dict[date] = [student_id]

    def generate_report(self,start_date,end_date):
        if self.Attendance_dict:
            for x,y in self.Attendance_dict.items():
                if x >= start_date and x <= end_date:
                    print(f"Date- {x}: Student ID of present student - {y}")
        else:
            print("No data available")

    def authentication(self):
        password = input("Enter password.\nIf not already Registered than register first as a Teacher\n")
        for teacher_data in self.Teacher_dict.values():
            print(teacher_data)
            if password == teacher_data[len(teacher_data)-1]:
                pass
            else:
                print("Incorrect password")
                break


choice = 1
while choice == 1:
    role = int(input("1)  Make entry as a Student\n"
                     "2)  Make entry as a Teacher\n"
                     "3)  Mark attendance\n"
                     "4)  Generate attendance report\n"
                     "0)  Exit\n"))
    

    if role == 1:
        std_choice = 1
        while std_choice != 0:
            data_choice = int(input("1)  Enter data\n"
                               "0)  Exit\n"))
            if data_choice == 1:
                student_input = input("Enter id,name,class,roll_number in the specified format\n"
                                      "NOTE:  it must be separated by comma\n").split(",")
                
                student_object = Student(f"{student_input[0]}",f"{student_input[1]}",f"{student_input[2]}",f"{student_input[3]}")

                if student_object.get_id() in Student.Student_dict.keys():
                    print("Error:  ID already exists. ID must be unique")
                else:
                    student_object.Student_dict[student_object.get_id()] = [student_object.get_name(),student_object.get_class(),\
                                                                           student_object.get_roll_number()]
                print(student_object.Student_dict)
                
            if data_choice == 0:
                std_choice = 0

    if role == 2:
        teach_choice = 1
        while teach_choice == 1:
            data_choice = int(input("1)  Enter data\n"
                               "0)  Exit\n"))
            if data_choice == 1:
                teacher_input = input("Enter id,name,subject_taught,set-password in the specified format\n"
                                      "NOTE:  it must be separated by comma\n").split(",")
                teacher_object = Teacher(f"{teacher_input[0]}",f"{teacher_input[1]}",f"{teacher_input[2]}",f"{teacher_input[3]}")
                
                if teacher_object.get_id() in Teacher.Teacher_dict.keys():
                    print("Error:  ID already exists. ID must be unique")
                else:
                    teacher_object.Teacher_dict[teacher_object.get_id()] = [teacher_object.get_name(),teacher_object.get_subject(),teacher_object.get_password()]
                print(teacher_object.Teacher_dict)

            if data_choice == 0:
                teach_choice = 0

    if role == 3:
        attendance_choice = 1
        while attendance_choice == 1:
                if not Teacher.Teacher_dict:
                    print("No registered teacher exist. Register first")
                else:
                    attendance_object = Attendance()
                    attendance_object.authentication()
                    attend_choice = 1
                    while attend_choice == 1:
                        att_choice = int(input("1)  Mark attendance\n"
                                            "0)  Exit\n"))
                        if att_choice == 1:
                            att_entry = input("Enter student_id and date separated by comma\n").split(",")
                            attendance_object.mark_attendance(att_entry[0],att_entry[1])
                            print(attendance_object.Attendance_dict)

                        if att_choice == 0:
                            attend_choice = 0
                            attendance_choice = 0

    if role == 4:
        report_choice = 1
        while report_choice == 1:
                if not Teacher.Teacher_dict:
                    print("No registered teacher exist. Register first")
                else:
                    attendance_object = Attendance()
                    attendance_object.authentication()
                    rprt_choice = 1
                    while rprt_choice == 1:
                        generate_choice = int(input("1)  Generate report\n"
                                                    "0)  Exit\n"))
                        
                        if generate_choice == 1:
                            date_entry = input("Enter start_date and end_date separated by comma\n").split(",")

                            attendance_object.generate_report(date_entry[0],date_entry[1])

                        if generate_choice == 0:
                            rprt_choice = 0
                            report_choice = 0

    if role == 0:
        choice = 0